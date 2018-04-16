from django.contrib import admin
from .models import Post

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'year',
        'studio',
        'slug',
        'genre',
        'active',
        'created',
        'updated',
        'timestamp',
        'get_age'
    ]
    readonly_fields = ['updated', 'timestamp', 'get_age']
    #def new_content (self, obj, *args,**kwargs):
    #    return str(obj.title)
    def get_age (self, obj,*args,**kwargs):
        return str(obj.age)
    class Meta:
            model = Post
admin.site.register(Post, PostModelAdmin)
