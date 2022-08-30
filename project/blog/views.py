from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def post_lists(request):
    posts = [
    {'name': 'Утро', 'text': 'Доброе утро'},
    {'name': 'День', 'text': 'Добрый день'},
    {'name': 'Вечер', 'text': 'Добрый вечер'},
    {'name': 'Ночь', 'text': 'Добрый ночь'},
]
    return render(request,'blog/index.html',context={'posts':posts})