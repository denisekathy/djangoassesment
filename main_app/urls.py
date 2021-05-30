from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name='index'),
    path('add/', views.ItemCreate.as_view(), name='add'),
    path('<int:item_id>/', views.items_detail, name='index'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='delete'),
]