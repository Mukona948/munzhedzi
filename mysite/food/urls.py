from . import views 
from django.urls import path

app_name = 'food'
urlpatterns = [
    #food path
    path('',views.index,name='index'),   
    #food 1 path
    path('<int:item_id>/',views.details,name='details'),
    path('item/',views.item,name='item'),
    # add items
    path('add',views.create_item,name='create_item'),
    #edit items as user
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item as user
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
    
]
