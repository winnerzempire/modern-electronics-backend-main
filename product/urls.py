from django.urls import path
from . import views
from .views import CategoryListCreateView, ProductListByCategory, category_list_view,  CategoryListCreateView, product_list_view, review_create_view, product_retrieve_view




urlpatterns = [
    path("api/categories/", category_list_view, name="category-list"),
    path("api/categories/class-based/", CategoryListCreateView.as_view(), name="category-list-cbv"),
    path("api/product/categories/", category_list_view, name="user-category-list"), 
    path("products/", product_list_view, name="product-list"),  # Lists all products
    path("products/<int:pk>/", product_retrieve_view, name="product-detail"),  # Retrieves a single product by its primary key
    path("reviews/create/", review_create_view, name="review-create"),  # Creates a new review
    path('products/category/selectedCategory/', ProductListByCategory.as_view(), name='products-by-category'),
    path('products/<int:category_id>/', ProductListByCategory.as_view(), name='product-list-by-category'),
]

