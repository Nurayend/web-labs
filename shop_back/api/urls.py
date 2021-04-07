from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.categories_list),
    path('categories/<int:category_id>/', views.category_details),
    path('categories/<int:category_id>/products/', views.products_list_by_category),
    path('products/', views.products_list),
    path('products/<int:product_id>/', views.product_details)
]