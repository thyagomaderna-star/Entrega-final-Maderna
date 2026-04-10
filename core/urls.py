from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.inicio, name='inicio'),
path('resgister/',views.registrar_usuario, name="register"),
path('login/', views.login_request, name='login'),
#Paths de equipos
path('equipo/list/', views.EquipoListView.as_view(), name='equipo_list'),
path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
path('equipo/nuevo/', views.EquipoCreateView.as_view(), name='equipo_create'),
path('equipo/editar/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_update'),
path('equipo/borrar/<int:pk>/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
#Paths de Posts
path('post/list/', views.PostListView.as_view(), name='post_list'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
path('post/nuevo/', views.PostCreateView.as_view(), name='post_create'),
path('post/editar/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
path('post/borrar/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)