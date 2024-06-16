#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    #http://127.0.0.1:8000/women/cats/music/?name=Gagarina&type=pop   (вернет список QueryDict в консоль)
    if request.GET:
        print(request.GET) 
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>404 Страница не найдена</h1>')
