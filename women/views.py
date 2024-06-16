from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    #http://127.0.0.1:8000/women/cats/music/?name=Gagarina&type=pop   (вернет список QueryDict в консоль)
    if request.GET:
        print(request.GET) 
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music', ))
        return redirect(uri, permanent=True) #перенаправление по коду 302 (только с первым параметром '<адрес на нужную стр>'); 
                                             #301 (при параметре permanent=true)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>404 Страница не найдена</h1>')
