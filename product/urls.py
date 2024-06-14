from django.urls import path
from . import views



urlpatterns = [
    path("", views.product_list_view, name="product-list"),
    path("create/", views.review_create_view, name="review-create"),
    path("<int:pk>", views.product_retrieve_view, name="product-detail")
]
