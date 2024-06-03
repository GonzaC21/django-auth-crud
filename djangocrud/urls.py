"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('lentes-de-lectura/', views.lentes_de_lectura, name='lentes-de-lectura'),
    path('lentes-deportivos/', views.lentes_deportivos, name='lentes-deportivos'),
    path('lentes-de-natacion/', views.lentes_de_natacion, name='lentes-de-natacion'),
    path('gafas-de-proteccion/', views.gafas_de_proteccion, name='gafas-de-proteccion'),
    path('lentes-de-ninos/', views.lentes_de_ninos, name='lentes-de-ninos'),
    path('lentes-de-tendencia/', views.lentes_de_tendencia, name='lentes-tendencia'),
    path('lentes-multifocales/', views.lentes_multifocales, name='lentes-multifocales'),
    path('lentes-de-sol/', views.lentes_de_sol, name='lentes-de-sol'),
    path('lentes-bluefilter/', views.lentes_Bluefilter, name='lentes-Bluefilter'),
    path('lentes-para-lejos/', views.lentes_para_Lejos, name='lentes-para-lejos'),
]
