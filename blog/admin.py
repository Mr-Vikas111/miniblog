from django.contrib import admin
from .models import Post,Contect
# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display =['id','title','desc','post_date','written_by']


@admin.register(Contect)

class ContectAdmin(admin.ModelAdmin):
    list_display =['id','name','email','address','message']