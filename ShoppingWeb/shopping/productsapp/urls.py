from django.urls import path
from productsapp import views

urlpatterns = [
    path('', views.index),
    path('product/details/<int:id>', views.ProductDetail , name='ProductDetail'),
    path('products/', views.products , name='products'),
]
 