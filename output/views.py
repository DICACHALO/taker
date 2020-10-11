from django.shortcuts import render, redirect
import io
import urllib, base64
from requeriments.models import RF, RnF
from .count import count_cost, count_priority, count_state
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from .plot import rfplot

def make_plot(rf, rnf):
    rf_count = len(rf)
    rnf_count = len(rnf)
    dic = {'R. Funcionales':rf_count, 'R. no Funcionales':rnf_count}
    state = count_state(rf, rnf)
    priority = count_priority(rf, rnf)
    cost = count_cost(rf, rnf)

    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    axs = axs.flatten()
    axs[0].pie(dic.values(), labels=dic.keys(), autopct="%0.1f %%")
    axs[0].set_title('Requerimientos')

    fig.suptitle('Gráficos Generales', fontsize=20)

    axs[1].pie(state.values(), labels=state.keys(), autopct="%0.1f %%")
    axs[1].set_title('Estado')

    axs[2].pie(cost.values(), labels=cost.keys(), autopct="%0.1f %%")
    axs[2].set_title('Costo')

    axs[3].pie(priority.values(), labels=priority.keys(), autopct="%0.1f %%")
    axs[3].set_title('Prioriodad')

    #plt.plot(range(10))
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close(fig)
    return uri


# Create your views here.
def plot(request, project_id):
    if request.user.is_authenticated:
        rf = RF.objects.filter(project=project_id)
        rnf = RnF.objects.filter(project=project_id)        
        uri = make_plot(rf, rnf)

        return render(request, "output/plot.html", {'data':uri, 'projecto':project_id})
    # En otro caso redireccionamos al login
    return redirect('/login')

def rf_plot(request, project_id):
    if request.user.is_authenticated:
        rf = RF.objects.filter(project=project_id)     
        uri = rfplot(rf)

        return render(request, "output/plot_rf.html", {'data':uri, 'projecto':project_id})
    # En otro caso redireccionamos al login
    return redirect('/login')

def rnf_plot(request, project_id):
    if request.user.is_authenticated:
        rnf = RnF.objects.filter(project=project_id)        
        uri = rfplot(rnf)

        return render(request, "output/plot_rnf.html", {'data':uri, 'projecto':project_id})
    # En otro caso redireccionamos al login
    return redirect('/login')

    