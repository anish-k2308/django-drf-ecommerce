from django.shortcuts import render
from rest_framework import viewsets,response
from .serializers import *
from .models import *
# Create your views here.


class CategoryViewset(viewsets.ViewSet):
    queryset = Category.objects.all()
    def list(self, request):
        serializer = CategorySerializer(self.queryset,many=True)
        return response.Response(serializer.data)