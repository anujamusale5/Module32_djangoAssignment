from django.shortcuts import render 
from django.views import View
from django.http import JsonResponse
from .data import products
from .serializers import ProductSerializer
class ProductList(View):
    def get(self,request):
        serialized_products=ProductSerializer(products,many=True).data
        return JsonResponse(products,safe=False)
# Create your views here.
