from django.shortcuts import render, Res
from rest_framework import viewsets,response
from serializers import *
from models import *
# Create your views here.


class CategoryViewset(viewsets.ViewSet):
    querryset = Category.objects.all()
    def list(self, request):
        serializer = CategorySerializer(self.querryset,many=True)
        return response.Response(serializer.data)