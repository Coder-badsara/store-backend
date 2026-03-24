from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view()
def product_list(request):
    product_list = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(product_list, many=True)
    return Response(serializer.data)

@api_view()
def products_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product) 
    return Response(serializer.data)

        