from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product'),
    path('create', views.create_list, name='create'),
    path('update/<int:id>/', views.update_list, name='update'),
    path('delete/<int:id>/', views.delete_list, name='delete'),
]