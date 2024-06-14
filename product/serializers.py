from rest_framework import serializers
from .models import Product, Category, Reviews
from api.serializers import UserSerializer
from .validators import unique_validator
import numpy as np


class CategorySerializer(serializers.ModelSerializer):
  admin=UserSerializer(source="user")
  title=serializers.CharField(validators=[unique_validator])
  class Meta:
    model=Category
    fields=(
      "id",
      "admin",
      "title"
    )
 
class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model=Reviews
    fields=(
      "id",
      "userName",
      "rating",
      "text",
      "created_at_formatted",
      "item_id"
    )
  
  
class ProductSerializer(serializers.ModelSerializer):
  category=CategorySerializer(read_only=True)
  reviews=serializers.SerializerMethodField(read_only=True)
  url=serializers.HyperlinkedIdentityField(
    view_name="product-detail",
    lookup_field="pk"
  )
  total_rating=serializers.SerializerMethodField(read_only=True)
  class Meta:
    model=Product
    fields=(
      "id",
      "url",
      "category",
      "productName",
      "imgUrl",
      "price",
      "initialPrice",
      "shortDisc",
      "description",
      "reviews",
      "total_rating",
      

      

    )

  def get_reviews(self, obj):
    q=Reviews.objects.filter(product_id=obj.pk)
    if q is not None:
      return ReviewSerializer(q, many=True, context=self.context).data
    return None
  def get_total_rating(self,obj):
    curr=Reviews.objects.filter(product_id=obj.id)
    acc=[]
    if curr is not None:
      item=0
      acc=[i.rating for i in curr if(i.product_id==obj.pk)]
    return np.sum(acc)
  
  
