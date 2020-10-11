from django.shortcuts import render, redirect
from .forms import ProjectForm, NewMember
from .models import Project, User_Project
from django.contrib.auth.models import User

# Create your views here.
def new_project(request):
    if request.user.is_authenticated:
        usuario = request.user
        project_form =ProjectForm()
        if request.method == 'POST':
            data=ProjectForm(request.POST)
            if data.is_valid():
                print(usuario)
                project = data.save(commit=False)
                project.save()
                data.save_m2m()
                many = User_Project()
                many.user = usuario
                many.project = project               
                many.save()
                print(project)
                return redirect("/projects")
        else:
            return render(request, "proyecto/create_project.html", {'form':project_form})
    else:
        return redirect('/login')

def projects(request):
    if request.user.is_authenticated:
        project = Project.objects.filter(user=request.user) 
        return render(request, "proyecto/show-projects.html", {'project':project})
    # En otro caso redireccionamos al login
    return redirect('/login')

def show_project(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id) 
        return render(request, "proyecto/show-project.html", {'projects':projects})
    # En otro caso redireccionamos al login
    return redirect('/login')

def group(request, project_id):

    if request.user.is_authenticated:
        projects = User_Project.objects.filter(project=project_id) 
        users = User_Project.objects.filter(user=request.user.id, project=project_id)
        proj = Project.objects.filter(id=project_id)
        return render(request, "proyecto/group.html", {'projects':projects,'proj':proj, 'users':users})
    # En otro caso redireccionamos al login
    return redirect('/login')

def new_member(request, project_id):
    if request.user.is_authenticated:
        form = NewMember()
        projects = Project.objects.filter(id=project_id)
        if request.method == 'POST':
            for project in projects:
                p = project
            data= request.POST
            member = User_Project()
            member.project = p
            users = User.objects.filter(username=data['user'])
            for user in users:
                u = user
            member.user = u
            member.type_user = data['type_user']
            member.save()
            return redirect("/group/"+str(project_id))
        return render(request, "proyecto/new-member.html", {'form':form, 'projects':projects })
    return redirect('/login')
