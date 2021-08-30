from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contect/', views.contect,name='contect'),
    path('deshboard/', views.deshboard,name='deshboard'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('addpost/', views.add_post,name='addpost'),
    path('updatepost/<int:id>', views.update_post,name='updatepost'),
    path('deletepost/<int:id>', views.delete_post,name='deletepost'),


]
