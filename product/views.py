from django.shortcuts import render
# Create your views here.
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.serializers import ProductSerializer
from rest_framework import viewsets
from product.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

 
class ProductList(APIView):
    def post(self, request):
        product = ProductSerializer(data=request.data, context={'request': request}) 
        if product.is_valid(raise_exception=True):
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
 
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={'request': request})  
        return Response({
            "product": serializer.data
        }, status=status.HTTP_200_OK)
    
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)