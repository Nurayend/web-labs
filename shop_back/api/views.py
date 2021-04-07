from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Product
from api.models import Category

# Create your views here.

def categories_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def category_details(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json())

def products_list_by_category(request, category_id):
    try:
        c = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    products = Product.objects.filter(category=c)
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)

def products_list(request):
    products = Product.objects.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)

def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())
