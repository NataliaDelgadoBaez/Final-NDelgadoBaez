from django.urls import path
from Tienda_app import views
from django.contrib.auth.views import LogoutView

#Generales
urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Soy nuevo"),
    path('logout/', LogoutView.as_view(template_name='Tienda_app/logout.html'), name="Logout"),
    #path('busca tu favorito/', views.Buscar_album, name="Busca tu favorito"),
    path('carrito/', views.carrito, name="Carrito"),
    path('carrito/', views.final_carrito, name="Fcarrito"),
    #path('crear album/', views.Agregaralbum, name="Crear album"),
    path('blog/', views.blog, name="Blog"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    path('conocenos/', views.conocenos, name="Conocenos"),
    #path('leerDisco', views.leer_disco, name = "LeerDisco")
]
    
# Discos
urlpatterns += [
    path('DiscoList/', views.DiscoList.as_view(), name="DiscoList"),
    path('DiscoDetail/<int:pk>/', views.DiscoDetail.as_view(), name="DiscoDetail"),
    path('DiscoCreate/', views.DiscoCreate.as_view(), name="DiscoCreate"),
    path('DiscoUpdate/<int:pk>/', views.DiscoUpdate.as_view(), name="DiscoUpdate"),
    path('DiscoDelete/<int:pk>/', views.DiscoDelete.as_view(), name="DiscoDelete"),
]