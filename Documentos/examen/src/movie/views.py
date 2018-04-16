from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .models import Post

import redis
r = redis.Redis (host='localhost', port=6379, db=0)

def sql_to_redis(request):
    m = Post.objects.all()

    ElCine = []

    for i in m:
        pelicula ={
        'Movies':{m.get(id=i.id).id: [m.get(id=i.id).name, m.get(id=i.id).year, m.get(id=i.id).studio, m.get(id=i.id).genre, m.get(id=i.id).active, m.get(id=i.id).created]}
        }

        ElCine.append(pelicula)

    r.set('Movies', ElCine)
    return redirect('/')

def home (request):
    context = {'Movies': r.get('Movies')}

    return render(request, 'index.html', context)
