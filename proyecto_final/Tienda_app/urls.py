from django.urls import path
from Tienda_app import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static



#Generales
urlpatterns = [
    
    path('conocenos/', views.about, name='Conocenos'),
    
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('login/', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='Tienda_app/logout.html'), name='Logout'),
    path('edituser/', views.edit, name="edituser"),

    path('soy nuevo/', views.register, name="Soy nuevo"),
    path('logout/', LogoutView.as_view(template_name='Tienda_app/logout.html'), name="Logout"),
    path('busca tu favorito/', views.Buscardisco, name="Busca tu favorito"),
    path('carrito/', views.carrito, name="Carrito"),
    path('carrito/', views.final_carrito, name="Fcarrito"),
    #path('crear album/', views.Agregaralbum, name="Crear album"),
    path('blog/', views.blog, name="Blog"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    
    path('creardisco/', views.creardisco, name="creardisco"),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
# Discos
urlpatterns += [
    path('DiscoList/', views.DiscoList.as_view(), name="DiscoList"),
    path('DiscoDetail/<int:pk>/', views.DiscoDetail.as_view(), name="DiscoDetail"),
    path('DiscoCreate/', views.DiscoCreate.as_view(), name="DiscoCreate"),
    path('DiscoUpdate/<int:pk>/', views.DiscoUpdate.as_view(), name="DiscoUpdate"),
    path('DiscoDelete/<int:pk>/', views.DiscoDelete.as_view(), name="DiscoDelete"),
]