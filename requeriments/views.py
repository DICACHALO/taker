from django.shortcuts import render, redirect
from proyecto.models import Project
from .forms import NewFunctionalrequeriments
from .models import RF, RnF
from proyecto.models import User_Project

# Create your views here.
def functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        requeriments = RF.objects.filter(project=project_id)
        users = User_Project.objects.filter(project=project_id, user=request.user.id)
        return render(request, "requeriments/functional_requeriments.html", {'projects':projects,'requeriments':requeriments, 'users':users })
    else:
        return redirect('/login')

def new_functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        form = NewFunctionalrequeriments()
        if request.method == 'POST':
            data= request.POST
            requeriments = RF()
            requeriments.title = data['title']
            for project in projects:
                p = project
            requeriments.project = p
            requeriments.description = data['description']
            requeriments.priority = data['priority']
            requeriments.state = data['state']
            requeriments.cost = data['cost']
            requeriments.comments = data['comments']
            requeriments.save()
            return redirect("/functional-requirements/"+str(project_id)+"/")
        return render(request, "requeriments/new_functional_requeriment.html", {'projects':projects,'form':form})
    else:
        return redirect('/login')

def no_functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        requeriments = RnF.objects.filter(project=project_id)
        users = User_Project.objects.filter(project=project_id, user=request.user.id)
        return render(request, "requeriments/no_functional_requeriments.html", {'projects':projects,'requeriments':requeriments,'users':users})
    else:
        return redirect('/login')

def new_non_functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        form = NewFunctionalrequeriments()
        if request.method == 'POST':
            data= request.POST
            requeriments = RnF()
            requeriments.title = data['title']
            for project in projects:
                p = project
            requeriments.project = p
            requeriments.type_r = data['type_r']
            requeriments.description = data['description']
            requeriments.priority = data['priority']
            requeriments.state = data['state']
            requeriments.cost = data['cost']
            requeriments.comments = data['comments']
            requeriments.save()
            return redirect("/non-functional-requirements/"+str(project_id)+"/")
        return render(request, "requeriments/new_nfunctional_requeriment.html", {'projects':projects,'form':form})
    else:
        return redirect('/login')


