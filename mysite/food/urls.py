from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # Food path
    path('', views.IndexClassView.as_view(), name='index'),   
    # Food details path
    path('<int:pk>/', views.DetailFood.as_view(), name='details'),
    path('item/', views.item, name='item'),
    # Add items
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # Edit items as user
    path('update/<int:id>/', views.update_item, name='update_item'),
    # Delete item as user
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
