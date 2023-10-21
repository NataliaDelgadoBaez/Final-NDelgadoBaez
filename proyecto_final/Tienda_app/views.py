from django.shortcuts import render
from Tienda_app.models import Disco, Carrito
from Tienda_app.forms import BuscarDiscoForm, UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Conoceme

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
                  return render(request,"Tienda_app/registro.html")

      else:
                 
            form = UserRegisterForm()     

      return render(request,"Tienda_app/registro.html" ,  {"form":form})

@login_required
def edit(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request,"Tienda_app/edituser_exitoso.html" )
        
    else:
        
        miFormulario = UserEditForm(initial={ 'email' : usuario.email})
        
    return render(request, "Tienda_app/edituser.html", {"miFormulario":miFormulario, "usuario":usuario}) 
    
# General
            
def inicio(request):
    return render(request, "Tienda_app/index.html")

def tienda(request):
    discos = Disco.objects.all()
    return render(request, "Tienda_app/tienda.html", {"discos": discos})

def blog(request):
    return render(request, "tienda_app/blog.html")

@login_required
def agregar_al_carrito(request, pk):
    producto = Disco.objects.get(id=pk)
    usuario = request.user

    # Verifica si el producto ya está en el carrito del usuario
    carrito_existente = Carrito.objects.filter(usuario=usuario, producto=producto)

    # Inicializa carrito
    carrito = None

    if carrito_existente.exists():
        # Si el producto ya está en el carrito, aumenta la cantidad
        carrito = carrito_existente.first()
        carrito.cantidad += 1
    else:
        # Si el producto no está en el carrito, crea un nuevo registro
        carrito = Carrito(usuario=usuario, producto=producto)

    # Guarda los cambios en la base de datos
    carrito.save()

    # Calcula el total del carrito de compras y obtiene todos los productos en el carrito junto con sus cantidades
    total = 0
    productos_carrito = []
    for item in Carrito.objects.filter(usuario=usuario):
        total += item.producto.precio * item.cantidad
        productos_carrito.append((item.producto, item.cantidad))

    return render(request, 'Tienda_app/agregar_al_carrito.html', {'total': total, 'productos_carrito': productos_carrito})

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
    
    def get_queryset(self):
        usuario_actual = self.request.user

        # Filtramos los discos que pertenecen al usuario actual
        queryset = Disco.objects.filter(user=usuario_actual)
        return queryset
    
class DiscoDetail(LoginRequiredMixin, DetailView):
    model = Disco
    template_name = "Tienda_app/DiscoDetail.html"
    context_object_name = "disco"
  
class DiscoCreate (LoginRequiredMixin, CreateView):
    model = Disco
    template_name = "Tienda_app/DiscoCreate.html"
    success_url = reverse_lazy("DiscoList")
    fields = ['imagen', 'nombre', 'autor', 'año', 'descripcion', 'precio','user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DiscoUpdate (LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "Tienda_app/DiscoUpdate.html"
    success_url = reverse_lazy("DiscoList")
    fields = ['nombre', 'autor', 'año', 'imagen','descripcion', 'precio']
   
class DiscoDelete (LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "Tienda_app/DiscoDelete.html"
    success_url = reverse_lazy ("DiscoList")
    
def Buscardisco(request):
    if request.method == "POST":
        miFormulario = BuscarDiscoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            discos = Disco.objects.filter(autor__icontains = informacion['autor'])

            return render(request, "Tienda_app/mostra_tu_favorito.html", {"discos": discos})
    else:
        miFormulario = BuscarDiscoForm()

    return render(request, "Tienda_app/busca_tu_favorito.html", {"miFormulario": miFormulario})

def creardisco(request):
    return render(request, "Tienda_app/creardisco.html")