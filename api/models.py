from django.db import models
from django.conf import settings


User=settings.AUTH_USER_MODEL
class Category(models.Model):
  user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  title=models.CharField(max_length=255)

class Reviews(models.Model):
  text=models.TextField()
  rating=models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
  category=models.ForeignKey(Category, default=1, related_name="category", on_delete=models.CASCADE)
  productName=models.CharField(max_length=255)
  imgUrl=models.ImageField(upload_to="media/")
  price=models.DecimalField(max_digits=10, decimal_places=2)
  shortDisc=models.CharField(max_length=100, null=True, blank=True)
  description=models.TextField()
  reviews=models.ForeignKey(Reviews, on_delete=models.CASCADE)
  avgRating=models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.productName





