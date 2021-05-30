from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item
from .forms import ItemForm
# Create your views here.


def items_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'


def items_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'index.html', {'item' : item })
    

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'

def showform(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {'form': form }
    return render(request, 'index.html', context)




