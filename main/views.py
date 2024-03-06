from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

# Create your views here.
#alt + shift + down скопировать текущую строку вниз


#представление или контроллер
def index (request):
    
    context = {
        'title': 'Home - Главная ',
        'content' : 'Магазин мебели Home',
    }
    return render(request, 'main/index.html',context)


def about (request):
    context = {
        'title': 'Home - О нас ',
        'content' : 'О нас',
        'text_on_page' : "Текст о магазине нашем"
    }
    return render(request, 'main/about.html',context)