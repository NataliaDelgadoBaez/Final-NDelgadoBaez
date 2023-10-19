from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import BuscarDiscoForm, UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# ACERCA DE MI

def about(request):
    return render(request, 'Tienda_app/conoceme.html', {})

# Acciones de usuario

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "Tienda_app/login bienvenida.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "Tienda_app/login.html", {"form": form, "msg_login": msg_login})

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

@login_required
def edit(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()


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
    template_name = "Tienda_app/DiscoList.html"
    
class DiscoDetail(LoginRequiredMixin, DetailView):
    model = Disco
    template_name = "Tienda_app/DiscoDetail.html"
    
class DiscoCreate (LoginRequiredMixin, CreateView):
    model = Disco
    template_name = "Tienda_app/DiscoCreate.html"
    success_url = reverse_lazy ("DiscoList")
    fields = ['nombre', 'autor', 'año', 'precio']

class DiscoUpdate (LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "Tienda_app/DiscoUpdate.html"
    success_url = reverse_lazy ("DiscoList")
    fields = ['nombre', 'autor', 'año']
    
class DiscoDelete (LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "Tienda_app/DiscoDelete.html"
    success_url = reverse_lazy ("DiscoList")
    

def Buscardisco(request):
    if request.method == "POST":
        miFormulario = BuscarDiscoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            discos = Disco.objects.filter(nombre__icontains = informacion['autor'])

            return render(request, "Tienda_app/mostra tu favorito.html", {"discos": discos})
    else:
        miFormulario = BuscarDiscoForm()

    return render(request, "Tienda_app/busca tu favorito.html", {"miFormulario": miFormulario})