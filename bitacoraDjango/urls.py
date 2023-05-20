"""bitacoraDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views
# import miapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('',views.index, name="index"),
        path('inicio/',views.index, name="inicio"),
    path('hola-mundo/', views.hola_mundo, name ="hola_Mundo"),
    path ('historial/', views.historial, name ="historial"), 
    path ('historial/<int:redirigir>', views.historial, name ="historial"),
    path ('crear-articulo/',views.crear_articulo, name="crear-articulo"),
    path ('crear-articulo/', views.crear_articulo,name="crear-articulo"),
    path('objeto/', views.objeto, name="objeto"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editar_articulo, name="editar"),
    path('articulos/',views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
        
    
]

