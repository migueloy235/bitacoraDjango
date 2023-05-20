from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import query
# Create your views here.


def index(request):

    return render(request, 'index.html')

def hola_mundo(request):
  return render(request,'hola_mundo.html')


def historial(request , redirigir=0):
  if redirigir==1:
    return redirect ('/hola-mundo/')
  return render(request,'historial.html')

def crear_articulo(request):
   articulo = Article( 
      title = 'ZAPATO',
      content = 'ROJO TALLA MEDIA ',
      public = True 
   )

   articulo.save()
   return HttpResponse("usuario creado: ")

def save_article(request, title, content, public):
   articulo = Article( 
      title = title,
      content = content,
      public = public
   )

   articulo.save()
   return HttpResponse("usuario creado: ")

def create_article(request):
   return render(request, 'create_article.html')


def objeto(request):
    return render(request, 'objeto.html')
   
def articulo(request):
  try:
   articulo = Article.objects.get(pk="21", public=True)
   response =f"Articulo: {articulo.id}. {articulo.title}  " 
 
  except:  
     response ="<h1>articulo no encontrado</h1>" 

  return HttpResponse(response)

def editar_articulo(request, id):
   articulo = Article.objects.get(pk=id)

   articulo.title ="Batman"
   articulo.content = "Pelicula del 2017"
   articulo.public = True

   articulo.save()

   return HttpResponse(f"Articulo editado: {articulo.id}. {articulo.title} ")

def articulos(request):
   articulos = Article.objects.order_by('title')
   articulos = Article.objects.filter(title="toalla")
  
   return render(request, 'articulos.html',{
  'articulos': articulos
})

def borrar_articulo(request,id):
   articulo = Article.objects.get(pk=id)
   articulo.delete()
   return redirect('articulos')  