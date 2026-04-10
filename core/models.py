from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField

#modelo del Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    año_fundacion = models.IntegerField(verbose_name="Año de Fundación")
    victorias = models.IntegerField(default=0, verbose_name="Partidos Ganados")
    escudo = models.ImageField(upload_to='escudos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

#El modelo del Perfil (Extensión del Usuario)
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.CharField(max_length=250, blank=True)
    equipo_favorito = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"



#Modelos de Post y comentarios
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150, blank=True)
    contenido = models.TextField()
    autor = models.CharField(max_length=50) 

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.post.titulo}"