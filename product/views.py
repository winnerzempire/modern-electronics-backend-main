from rest_framework import generics
from .serializers import ProductSerializer, ReviewSerializer
from .models import Product, Reviews
from rest_framework import serializers
from api.mixins import StaffEditorPermissionsMixin

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
