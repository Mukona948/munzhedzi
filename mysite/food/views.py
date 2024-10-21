from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("<h1>Welcome to TomTom</h1>")

def details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/details.html', context)

class DetailFood(DetailView):
    model = Item
    template_name = 'food/details.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item created successfully.')
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        messages.success(self.request, 'Item created successfully.')
        self.object = form.save()
        return redirect('food:details',pk=self.object.pk)

def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Item updated successfully.')
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item})
