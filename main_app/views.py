from main_app.models import Item
from django.shortcuts import render
from django.views.generic.edit import CreateView


# Create your views here.
class ItemCreate(CreateView):
    model = Item
    fields  = '__all__'

def home(request):
   return render(request, 'home.html')

def add(request):
    return render(request,'add.html' )

def items_index(request):
    items = Item.objects.all()
    return render(request, 'items_index.html', {'items': items})



