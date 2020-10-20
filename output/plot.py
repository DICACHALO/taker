from .count import count_rcost, count_rpriority, count_rstate
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import io
import urllib, base64


def rfplot(rf):


    state = count_rstate(rf)
    priority = count_rpriority(rf)
    cost = count_rcost(rf)
 
    ax1 = plt.subplot(212)
    ax1.pie(state.values(), labels=state.keys(), autopct="%0.1f %%")
    ax1.set_title('Estado')

    ax2 = plt.subplot(221)
    ax2.pie(priority.values(), labels=priority.keys(), autopct="%0.1f %%")
    ax2.set_title('Prioridad')

    ax3 = plt.subplot(222)
    ax3.pie(cost.values(), labels=cost.keys(), autopct="%0.1f %%")
    ax3.set_title('Costo')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close(fig)
    return uri