from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

def index(request):
    data = {
        'title': 'Главная страница', 
        'menu': menu,
        'posts': data_db,
        }
    #t = render_to_string('women/index.html')
    #return HttpResponse(t)   эти две строки - сокращенный вариант строки ниже
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {
        'title': 'О сайте' 
        }
    return render(request, 'women/about.html', data)

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
