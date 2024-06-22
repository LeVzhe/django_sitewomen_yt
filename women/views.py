from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound

menu = [
        {'title':"О сайте", 'url_name':'about'}, 
        {'title':"Добавить статью", 'url_name':'add_page'}, 
        {'title':"Обратная связь", 'url_name':'contact'}, 
        {'title':"Войти", 'url_name':'login'},
    ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''Анджелина Джоли — американская актриса, режиссёр, продюсер и гуманитарный активист. 
     Обладательница множества кинематографических наград и признания за свою гуманитарную деятельность.''', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': '''Марго Робби - австралийская актриса и фильмопродюсер, получившая известность благодаря своим ролям в таких фильмах, как "Волк с Уолл-стрит", "Отряд самоубийц" и "Тоня против всех".''', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': '''Джу́лия Фионо́ра Ро́бертс — американская актриса и продюсер, ставшая известной благодаря ролям в романтических комедиях и фильмах различных жанров. 
     Её карьера включает в себя такие фильмы, как "Прекрасная жизнь", "Предложение", "Эрин Брокович" и многие другие.''', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
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
        'title': 'О сайте',
        'menu': menu 
        }
    return render(request, 'women/about.html', data)

def addpage(request):
    return HttpResponse(f"Отображение addpage")


def contact(request):
    return HttpResponse(f"Отображение contact")


def login(request):
    return HttpResponse(f"Отображение login")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с ID = {post_id}")

def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с ID = {cat_id}")


    

# def categories(request, cat_id):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

# def categories_by_slug(request, cat_slug):
#     #http://127.0.0.1:8000/women/cats/music/?name=Gagarina&type=pop   (вернет список QueryDict в консоль)
#     if request.GET:
#         print(request.GET) 
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

# def archive(request, year):
#     if year > 2024:
#         uri = reverse('cats', args=('music', ))
#         return redirect(uri, permanent=True) #перенаправление по коду 302 (только с первым параметром '<адрес на нужную стр>'); 
#                                              #301 (при параметре permanent=true)
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>404 Страница не найдена</h1>')
