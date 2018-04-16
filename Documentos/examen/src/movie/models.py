from __future__ import unicode_literals
from django.utils.encoding import smart_text
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from .validators import validate_studio
from datetime import timedelta,datetime,date,time
from django.utils.timesince import timesince

GENRE_TIPO = (
        ('T', 'Terror'),
        ('C', 'Ciencia ficcion'),
        ('F', 'Fantasia'),
        ('A', 'Accion'),
        ('D', 'Animado')
    )

class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def nuevo_name_items(self, value):
        return self.filter(name_icontains = value)

class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using = self._db)

    def all(self, *args, **kwargs):
        qs = super(PostModelManager,self).all(*args, **kwargs).active()
        return (qs)

# Create your models here.

class Post(models.Model):
    #id=models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    name   = models.CharField(max_length=120, default="Nombre de la pelicula",unique=True,error_messages={"unique":"Este titulo no es unico, intenta de nuevo"},help_text='Debe ser un titulo unico',verbose_name='Post')
    year   = models.CharField(max_length=120, default="2018")
    studio = models.CharField(max_length=120,validators=[validate_studio],null=True,blank=True)
    genre = models.CharField(max_length=120, choices=GENRE_TIPO, default="M")
    slug   = models.SlugField(null=True,blank=True)
    active = models.BooleanField(default=False)
    updated= models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now = False,auto_now_add=False,default=timezone.now)

    objects = PostModelManager()


    def __str__(self):
        return smart_text(self.name)

    def save(self, *args, **kwargs):
        print('Guarde algo en el examen')
        if not self.slug:
            if self.name:
                self.slug=slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    @property
    def age(self):
        if self.genre!='':
            now=datetime.now()
            print("NOW:"+str(now))
            createdtime=datetime.combine(self.created, datetime.now().time())
            try:
                difference=now-createdtime
            except:
                return "Desconocido"
            if difference <= timedelta(minutes=1):
                return 'Hoy'
            #return '{time} ago.'.format(time=timesince(createdtime).split(',')[0])
            return createdtime
        return "no publicado"

def post_model_pre_save_receiver(sender,instance,*args,**kwargs):
    print('Antes de almacenar en el examen')
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)
        instance.save()
pre_save.connect(post_model_pre_save_receiver,sender=Post)

def post_model_post_save_receiver(sender,instance,created,*args,**kwargs):
    print("Despues-almacenar")
    if not instance.slug and instance.name:
        instance.slug=slugify(instance.name)
        instance.save()
post_save.connect(post_model_post_save_receiver, sender=Post)
