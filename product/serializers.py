from rest_framework import serializers
from .models import Product, Category, Reviews
from api.serializers import UserSerializer
from .validators import unique_validator
import numpy as np
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CategorySerializer(serializers.ModelSerializer):
    admin = UserSerializer(source="user")  # Linking to the User model
    title = serializers.CharField(validators=[unique_validator])  # Ensuring unique titles
    
    class Meta:
        model = Category
        fields = ("id", "admin", "title")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = (
            "id",
            "userName",
            "rating",
            "text",
            "created_at_formatted",
            "item_id"
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested Category serializer
    reviews = serializers.SerializerMethodField(read_only=True)  # Using a method for reviews
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    shortDiscList = serializers.SerializerMethodField()  # Method to split short descriptions
    total_rating = serializers.SerializerMethodField(read_only=True)  # Total ratings

    class Meta:
        model = Product
        fields = [
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
            "shortDiscList",  # Include shortDiscList here
        ]
    
    def get_reviews(self, obj):
        """Fetch reviews for a product."""
        reviews = Reviews.objects.filter(product_id=obj.pk)
        return ReviewSerializer(reviews, many=True, context=self.context).data if reviews.exists() else []

    def get_total_rating(self, obj):
        """Calculate the total rating based on the reviews."""
        reviews = Reviews.objects.filter(product_id=obj.id)
        return sum([review.rating for review in reviews]) if reviews.exists() else 0

    def create(self, validated_data):
        """Custom create method (if needed)"""
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def get_shortDiscList(self, obj):
        """Return a list of short descriptions from 'shortDisc'."""
        if obj.shortDisc:
            return [line.strip() for line in obj.shortDisc.split('\n') if line.strip()]
        return []

