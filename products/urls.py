from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),

]
