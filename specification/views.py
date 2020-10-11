from django.shortcuts import render, redirect
from proyecto.models import Project, User_Project
from requeriments.models import RF, RnF
from .models import SRF, SRnF, SRFFile, SRnFFile
from .forms import SpecificRequeriment, SpecificnFRequeriment, SpecificRequerimentFeed, NonSpecificRequerimentFeed


# Create your views here.
def functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        specifications = SRF.objects.filter(project=project_id)
        requeriments = RF.objects.filter(project=project_id).exclude(specific=True)

        users = User_Project.objects.filter(project=project_id, user=request.user.id)
        return render(request, "specification/specific_requeriments.html", {'projects':projects,'requeriments':requeriments, 'users':users, 'specifications':specifications })
    else:
        return redirect('/login')

def especific_requerimen(request, requeriment_id):
    if request.user.is_authenticated:
        requeriments = RF.objects.filter(id=requeriment_id)
        
        form = SpecificRequeriment()
        feed_form = SpecificRequerimentFeed()
        if request.method == 'POST':
            for requeriment in requeriments:
                data = request.POST
                object_specific = SRF()
                object_specific.title = requeriment.title
                object_specific.input = data['input'] 
                object_specific.source = data['source'] 
                object_specific.output = data['output']
                object_specific.destiny = data['destination'] 
                object_specific.restriction = data['restriction'] 
                object_specific.collateral_damage = data['collateral_damage'] 
                object_specific.process = data['process'] 
                object_specific.project = requeriment.project
                object_specific.description = requeriment.description
                object_specific.priority = requeriment.priority
                object_specific.state = requeriment.state
                object_specific.cost = requeriment.cost
                object_specific.comments = requeriment.comments
                object_specific.rf = requeriment

                
                file_form = SpecificRequerimentFeed(request.POST, request.FILES)
                files = request.FILES.getlist('file') #field name in model
                if file_form.is_valid():
                    for f in files:
                        file_instance = SRFFile(file=f, rf=requeriment)
                        file_instance.save()
                object_specific.save()
                requeriment.specific = True
                requeriment.save()
                project_id = requeriment.project.id
                return redirect("/specification-functional-requirements/"+str(project_id)+"/")
        return render(request, "specification/specific_requeriment.html", {'form':form,'requeriments':requeriments,'feed_form':feed_form})
    else:
        return redirect('/login')

def non_functional_requeriment(request, project_id):
    if request.user.is_authenticated:
        projects = Project.objects.filter(id=project_id)
        specifications = SRnF.objects.filter(project=project_id)
        requeriments = RnF.objects.filter(project=project_id).exclude(specific=True)
        users = User_Project.objects.filter(project=project_id, user=request.user.id)
        return render(request, "specification/specific_nf_requeriments.html", {'projects':projects,'requeriments':requeriments, 'users':users, 'specifications':specifications })
    else:
        return redirect('/login')

def especific_nf_requerimen(request, requeriment_id):
    if request.user.is_authenticated:
        requeriments = RnF.objects.filter(id=requeriment_id)
        form = SpecificnFRequeriment()
        feed_form = NonSpecificRequerimentFeed()
        if request.method == 'POST':
            for requeriment in requeriments:
                data = request.POST
                object_specific = SRnF()
                object_specific.title = requeriment.title
                object_specific.sub_type = data['sub_type'] 
                object_specific.project = requeriment.project
                object_specific.description = requeriment.description
                object_specific.priority = requeriment.priority
                object_specific.state = requeriment.state
                object_specific.cost = requeriment.cost
                object_specific.type_r = requeriment.type_r
                object_specific.comments = requeriment.comments
                object_specific.rnf = requeriment
                file_form = NonSpecificRequerimentFeed(request.POST, request.FILES)
                files = request.FILES.getlist('file') #field name in model
                if file_form.is_valid():
                    for f in files:
                        file_instance = SRnFFile(file=f, rnf=requeriment)
                        file_instance.save()
                object_specific.save()
                requeriment.specific = True
                requeriment.save()
                project_id = requeriment.project.id
                return redirect("/specification-non-functional-requirements/"+str(project_id)+"/")
        return render(request, "specification/specific_nf_requeriment.html", {'form':form,'requeriments':requeriments,'feed_form':feed_form})
    else:
        return redirect('/login')

def see_fr(request, requeriment_id):
    if request.user.is_authenticated:
        specifications = SRF.objects.filter(rf=requeriment_id)
        requeriments = RF.objects.filter(id=requeriment_id)
        for requeriment in requeriments:
            r = requeriment
        feeds = SRFFile.objects.filter(rf=r)
        return render(request, "specification/see_functional_requeriment.html", {'feeds':feeds, 'specifications':specifications })
    else:
        return redirect('/login')

def see_nfr(request, requeriment_id):
    if request.user.is_authenticated:
        specifications = SRnF.objects.filter(rnf=requeriment_id)
        requeriments = RnF.objects.filter(id=requeriment_id)
        for requeriment in requeriments:
            r = requeriment
        feeds = SRnFFile.objects.filter(rnf=r)
        return render(request, "specification/see_non_functional_requeriment.html", {'feeds':feeds, 'specifications':specifications })
    else:
        return redirect('/login')
  
def download():
    print('x')


