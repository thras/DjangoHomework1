from django.http import JsonResponse
from django.shortcuts import render

from .models import Manufacturer, Product

# Return all the ACTIVE manufacturers
def manufacturer_list(request):

    manufacturer = Manufacturer.objects.all()
    data = {"manufacturer": list(manufacturer.values("pk","name", "active").filter(active=True))} 
    response = JsonResponse(data)
    return response

# Return the details of a manufacturer with the a list of the products that he manufacturing
def manufacturer_detail(request, pk): 
    try:
        manufacturers = Manufacturer.objects.get(pk=pk) 
        products = Product.objects.all().filter(manufacturer = pk)
        # products=   products.filter(manufacturer = manufacturers.name )
        data = {"manufacturer": {
                "name": manufacturers.name,
                "location": manufacturers.location, 
                "active": manufacturers.active,
                "products": list(products.values("name")),
        }}
        response = JsonResponse(data) 
    except Product.DoesNotExist:
        response = JsonResponse({ "error": {
                            "code": 404,
                            "message" : "manufacturer not found!" }},
                            status=404) 
    return response


# Retunr a list of all products
def product_list(request):

    products = Product.objects.all()
    data = {"products": list(products.values("pk","name"))} 
    response = JsonResponse(data)
    return response

# Return the details of a product
def product_detail(request, pk): 
    try:
        product = Product.objects.get(pk=pk) 
        data = {"product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name, 
                "description": product.description,
                "price": product.price,
        }}
        response = JsonResponse(data) 
    except Product.DoesNotExist:
        response = JsonResponse({ "error": {
                            "code": 404,
                            "message" : "product not found!" }},
                            status=404) 
    return response