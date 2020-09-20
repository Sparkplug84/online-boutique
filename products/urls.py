from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # Adding int: to the product detail ensures the url is a number as navigating
    # add/ will interpret the string as an id and throw an error
    path('add/', views.add_product, name='add_product'),
]
