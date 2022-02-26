from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class ProductList(APIView):

    def get(self, request):
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetails(APIView):

    def get(self, request, pk):
        try:
            data = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data)
            return Response(serializer.data)
        except:
            return Response({'error': 'Product not found !!!'},status=status.HTTP_404_NOT_FOUND)