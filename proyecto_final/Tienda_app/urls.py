from django.urls import path
from Tienda_app import views
from django.contrib.auth.views import LogoutView


# Generales
urlpatterns = [
    
    path('conocenos/', views.about, name='Conocenos'),
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.final_carrito, name="Fcarrito"),
    path('blog/', views.blog, name="Blog"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    
# Usuarios   
    
    path('login/', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='Tienda_app/logout.html'), name='Logout'),
    path('edituser/', views.edit, name="edituser"),
    path('registro/', views.register, name="registro"),
    path('logout/', LogoutView.as_view(template_name='Tienda_app/logout.html'), name="Logout"),
]


# Discos
urlpatterns += [
    path('DiscoList/', views.DiscoList.as_view(), name="DiscoList"),
    path('DiscoDetail/<int:pk>/', views.DiscoDetail.as_view(), name="DiscoDetail"),
    path('DiscoCreate/', views.DiscoCreate.as_view(), name="DiscoCreate"),
    path('DiscoUpdate/<int:pk>/', views.DiscoUpdate.as_view(), name="DiscoUpdate"),
    path('DiscoDelete/<int:pk>/', views.DiscoDelete.as_view(), name="DiscoDelete"),
    path('busca_tu_favorito/', views.Buscardisco, name="busca_tu_favorito"),
    path('creardisco/', views.creardisco, name="creardisco"),
]