"""taker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from proyecto import views as view_project
from django.conf.urls.static import static
from requeriments import views as requeriments_views
from specification import views as specification_requeriments
from output import views as output, pdf

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('new-project', view_project.new_project, name="new_project"),
    path('projects', view_project.projects, name="projects"),
    path('project/<int:project_id>', view_project.show_project, name="project"),
    path('group/<int:project_id>/', view_project.group, name="group"),
    path('new-member/<int:project_id>/', view_project.new_member, name="new_member"),
    path('functional-requirements/<int:project_id>/', requeriments_views.functional_requeriment, name="functional_requeriments"),
    path('new-functional-requirement/<int:project_id>/', requeriments_views.new_functional_requeriment, name="new_fr"),
    path('non-functional-requirements/<int:project_id>/', requeriments_views.no_functional_requeriment, name="no_functional_requeriments"),
    path('new-non-functional-requirement/<int:project_id>/', requeriments_views.new_non_functional_requeriment, name="new_nfr"),
    path('specification-functional-requirements/<int:project_id>/', specification_requeriments.functional_requeriment, name="sfrs"),
    path('specification-functional-requirement/<int:requeriment_id>/', specification_requeriments.especific_requerimen, name="sfr"),
    path('specification-non-functional-requirements/<int:project_id>/', specification_requeriments.non_functional_requeriment, name="snfrs"),
    path('specification-non-functional-requirement/<int:requeriment_id>/', specification_requeriments.especific_nf_requerimen, name="snfr"),
    path('graph/<int:project_id>/', output.plot, name="plot"),
    path('graph-functional-requeriment/<int:project_id>/', output.rf_plot, name="prf"),
    path('graph-non-functional-requeriment/<int:project_id>/', output.rnf_plot, name="prnf"),
    path('see-functional-requeriment/<int:requeriment_id>/', specification_requeriments.see_fr, name="ffr"),
    path('see-non-functional-requeriment/<int:requeriment_id>/', specification_requeriments.see_nfr, name="fnfr"),

    path('admin/', admin.site.urls),
    path('media/', specification_requeriments.download),
    path('pdf/', pdf.pdf, name="pdf"),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)