from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from store import serializers as auth_serializer
from store import models as store_model


class CateogoryListAPIView(generics.ListAPIView):
    serializer_class = auth_serializer.CategorySerializer
    queryset = store_model.Category.objects.all()
