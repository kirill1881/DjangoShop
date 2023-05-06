from django.shortcuts import render, redirect

from . import models


# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_item(request):
    if request.method == 'POST':
        item = models.Item()
        item.name = request.POST.get('name')
        item.disk = request.POST.get('disc')
        item.img = request.POST.get('img')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/')
    return render(request, 'addItem.html')