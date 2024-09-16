from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer
from .models import Product, Reviews, Category
from rest_framework import serializers
from api.mixins import StaffEditorPermissionsMixin
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
category_list_view = CategoryListCreateView.as_view()

class ListAPIView(generics.ListAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
product_list_view=ListAPIView.as_view()

class CreateAPIView(generics.CreateAPIView):
  queryset=Reviews.objects.all()
  serializer_class=ReviewSerializer
  def perform_create(self,serializer):
    id=serializer.validated_data.get("item_id")
    product=Product.objects.get(pk=int(id))
    serializer.save(product=product)
 
review_create_view=CreateAPIView.as_view()


class RetrieveAPIView(StaffEditorPermissionsMixin,
                      generics.RetrieveAPIView):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  lookup_field="pk"

product_retrieve_view= RetrieveAPIView.as_view()





class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # Get category_id from URL
        return Product.objects.filter(category_id=category_id)

