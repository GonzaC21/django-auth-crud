from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task

from .forms import TaskForm

from django.http import JsonResponse

import json
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def lista_productos(request): 
    productos_json = '''
    {
      "productos": [
        {
          "productId": 301,
          "Descripcion": "Lentes de Lectura",
          "Preciocosto": "3000",
          "Precio": "6000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/LXBGbNqj/lentes-bluefilter.jpg",
          "ProductName": "Lentes de Lectura",
          "ProductPrice": "$60.00",
          "ProductDescripcion": "Lentes de lectura con aumento, disponibles en varios grados.",
          "ProductDetalle": "Elegantes y funcionales, ideales para leer libros y revistas.",
          "id": "301"
        },
        {
          "productId": 302,
          "Descripcion": "Lentes Deportivos",
          "Preciocosto": "7000",
          "Precio": "10000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/JzSwDyVH/gafas-deportivas.jpg",
          "ProductName": "Lentes Deportivos",
          "ProductPrice": "$100.00",
          "ProductDescripcion": "Lentes diseñados para actividades deportivas, ofrecen protección y visión clara.",
          "ProductDetalle": "Incluye estuche deportivo y cinta ajustable.",
          "id": "302"
        },
        {
          "productId": 303,
          "Descripcion": "Lentes de Natación",
          "Preciocosto": "11000",
          "Precio": "16000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/rwDXw1bL/gafas-natacion.jpg",
          "ProductName": "Lentes de Natación",
          "ProductPrice": "$160.00",
          "ProductDescripcion": "Lentes diseñados para natación, proporcionan visión clara bajo el agua.",
          "ProductDetalle": "Disponibles en diferentes tamaños y estilos.",
          "id": "303"
        },
        {
          "productId": 304,
          "Descripcion": "Gafas de Protección",
          "Preciocosto": "15000",
          "Precio": "18000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/63NDcDQ9/gafas-de-proteccion.jpg",
          "ProductName": "Gafas de Protección",
          "ProductPrice": "$180.00",
          "ProductDescripcion": "Gafas de seguridad para protección ocular en entornos peligrosos.",
          "ProductDetalle": "Resistentes a impactos y ralladuras.",
          "id": "304"
        },
        {
          "productId": 305,
          "Descripcion": "Lentes de Niños",
          "Preciocosto": "17000",
          "Precio": "20000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/HWzf0v1g/lentes-de-ni-o.jpg",
          "ProductName": "Lentes de Niños",
          "ProductPrice": "$200.00",
          "ProductDescripcion": "Lentes diseñados especialmente para niños, cómodos y resistentes.",
          "ProductDetalle": "Disponibles en colores y diseños divertidos.",
          "id": "305"
        },
        {
          "productId": 306,
          "Descripcion": "Lentes de Tendencia",
          "Preciocosto": "22000",
          "Precio": "25000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/VkhwqGM6/product-lentestendencia.jpg",
          "ProductName": "Lentes de Tendencia",
          "ProductPrice": "$250.00",
          "ProductDescripcion": "Lentes de moda con diseños exclusivos y materiales de calidad.",
          "ProductDetalle": "Únete a la última tendencia en gafas de sol y graduadas.",
          "id": "306"
        },
        {
          "productId": 307,
          "Descripcion": "Lentes Multifocales",
          "Preciocosto": "27000",
          "Precio": "30000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/m2rKm3TF/lentes-multifocal.jpg",
          "ProductName": "Lentes Multifocales",
          "ProductPrice": "$300.00",
          "ProductDescripcion": "Lentes con múltiples focos de visión para corregir la presbicia.",
          "ProductDetalle": "Incluye tratamientos antirreflejos y anti-ralladuras.",
          "id": "307"
        },
        {
          "productId": 308,
          "Descripcion": "Lentes de Sol",
          "Preciocosto": "25000",
          "Precio": "28000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/g0hCvYmS/lente-de-sol.jpg",
          "ProductName": "Lentes de Sol",
          "ProductPrice": "$280.00",
          "ProductDescripcion": "Lentes de sol para protección contra los rayos UV y el deslumbramiento.",
          "ProductDetalle": "Disponibles en diferentes estilos y colores.",
          "id": "308"
        },
        {
          "productId": 309,
          "Descripcion": "Lentes Bluefilter",
          "Preciocosto": "17000",
          "Precio": "20000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/LXBGbNqj/lentes-bluefilter.jpg",
          "ProductName": "Lentes Bluefilter",
          "ProductPrice": "$200.00",
          "ProductDescripcion": "Lentes con filtro de luz azul para proteger los ojos de la fatiga digital.",
          "ProductDetalle": "Diseñados para uso prolongado frente a pantallas.",
          "id": "309"
        },
        {
          "productId": 310,
          "Descripcion": "Lentes para Lejos",
          "Preciocosto": "37000",
          "Precio": "40000",
          "Fechaingreso": "01/03/2023",
          "ProductImage": "https://i.postimg.cc/hv26Sv1j/lentes-de-lejos.jpg",
          "ProductName": "Lentes para Lejos",
          "ProductPrice": "$400.00",
          "ProductDescripcion": "Lentes diseñados para una visión clara a larga distancia.",
          "ProductDetalle": "Ideales para actividades al aire libre y deportes.",
          "id": "310"
        },
        {
          "productId": 311,
          "id": "311"
        }
      ]
    }
    '''
    return JsonResponse(json.loads(productos_json))