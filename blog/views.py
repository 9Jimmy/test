from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
    'title': 'Our first post',
    'text': 'Just large text for the first post',
    'date': '1 January 2019',
    'autor': ''
    },
    {
    'title': 'Our second post',
    'text': 'Just large text for the second post',
    'date': '2 January 2019',
    'autor': 'Jimmy'
    }
]

def home(request):
    data = {
        'news': news,
        'title': 'Main blog\'s page'
    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'About us'})
