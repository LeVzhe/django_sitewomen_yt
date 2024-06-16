from django.urls import path, register_converter

from . import views

from . import converters #импорт файла конвертора для регулярных url-запросов


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive),
]
