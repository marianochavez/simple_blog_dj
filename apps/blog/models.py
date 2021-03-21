from django.db import models
from django.db.models.fields import EmailField
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombre categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField(
        'Categoria activada/desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        'Nombre Autor', max_length=255, null=False, blank=False)
    apellido = models.CharField(
        'Apellido Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook Autor', null=True, blank=True)
    twitter = models.URLField('Twitter Autor', null=True, blank=True)
    isntagram = models.URLField('Instagram Autor', null=True, blank=True)
    web = models.URLField('Web Autor', null=True, blank=True)
    email = EmailField('Email Autor', null=False, blank=False)
    estado = models.BooleanField(
        'Autor activo/noActivo', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0}, {1}".format(self.apellido,self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=90,blank=False,null=False)
    slug = models.CharField('Slug',max_length=100,blank=False,null=False)
    descripcion = models.CharField('Descripcion',max_length=110,blank=False,null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255,null=False,blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado',default=True)
    fecha_creacion = models.DateField('Fecha creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

