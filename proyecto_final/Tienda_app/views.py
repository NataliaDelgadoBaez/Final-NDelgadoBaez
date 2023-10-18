from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import Crearalbumform, Buscaralbumform, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Acciones de usuario

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            nombre_usuario = authenticate(username= usuario, password=clave)

            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "Tienda_app/tienda.html", {"mensaje":f"Has iniciado sesion, Bienvenido {usuario}"})
            else:
                return render(request, "Tienda_app/login.html", {"mensaje":"Usuario o contraseña incorrecta"})
           
        else:

            return render(request,"Tienda_app/login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Tienda_app/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Tienda_app/register.html")

      else:
                 
            form = UserRegisterForm()     

      return render(request,"Tienda_app/soy nuevo.html" ,  {"form":form})

def inicio(request):
    return render(request, "Tienda_app/index.html")

def tienda(request):
    return render(request, "Tienda_app/tienda.html")

def blog(request):
    return render(request, "tienda_app/blog.html")

@login_required
def carrito(request):
    return render(request, "Tienda_app/carrito.html")

def final_carrito(request):
    return render(request, "Tienda_app/fcarrito.html")

def iniciar_sesion(request):
    return render(request, "Tienda_app/login.html")

def musica_siempre(request):
    return render(request, "Tienda_app/Musica de siempre.html")

def musica_hoy(request):
    return render(request, "Tienda_app/Musica de hoy.html")

def conocenos(request):
    return render(request, "Tienda_app/conocenos.html")

def entrevistas(request):
    return render(request, "Tienda_app/entrevistas.html")


#Acciones con el disco

class DiscoList (LoginRequiredMixin, ListView):
    model = Disco
    template_name = "Tienda_app/ DiscoList.html"
    
class DiscoDetail(LoginRequiredMixin, DetailView):
    model = Disco
    template_name = "Tienda_app/ disco_detalles.html"
    
class DiscoCreate (LoginRequiredMixin, CreateView):
    model = Disco
    template_name = "Tienda_app/ DiscoCreate.html"
    success_url = reverse_lazy ("list")
    fields = ['nombre', 'autor', 'año', 'precio']

class DiscoUpdate (LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "Tienda_app/ disco_edicion.html"
    success_url = reverse_lazy ("list")
    fields = ['nombre', 'autor', 'año']
    
class DiscoDelete (LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "Tienda_app/ disco_borrado.html"
    success_url = reverse_lazy ("list")
    
