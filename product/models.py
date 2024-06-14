from django.db import models
from django.conf import settings
from django.utils.timesince import timesince

User=settings.AUTH_USER_MODEL
class Category(models.Model):
  user=models.ForeignKey(User, related_name="user_id", null=True, 
                         on_delete=models.SET_NULL)
  title=models.CharField(max_length=255)
  class Meta:
    verbose_name_plural="Categories"
  def __str__(self):
    return self.title



class Product(models.Model):
  category=models.ForeignKey(Category, default=1, 
                             related_name="product_category", 
                             on_delete=models.CASCADE)
  productName=models.CharField(max_length=255, default="")
  imgUrl=models.ImageField(upload_to="media/", null=True)
  price=models.DecimalField(max_digits=10, decimal_places=2, default=0)
  initialPrice=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  shortDisc=models.CharField(max_length=100, null=True, blank=True)
  description=models.TextField(blank=True, null=True)
  created_at=models.DateTimeField(auto_now_add=True)
  avgRating=models.DecimalField(max_digits=10, null=True, 
                                blank=True, decimal_places=2)
  
  

  class Meta:
    ordering=("-created_at",)

  def __str__(self):
    return self.productName
  def created_at_formatted(self):
    return timesince(self.created_at)

class Reviews(models.Model):
 
  userName=models.CharField(max_length=100, default="")
  product=models.ForeignKey(Product,default="", 
                                 related_name="product_review", 
                                 on_delete=models.CASCADE, null=True, blank=True)
  text=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)
  rating=models.DecimalField(max_digits=10, decimal_places=2)
  item_id=models.IntegerField(default=0)
  class Meta:
    ordering=("-created_at",)
    verbose_name_plural="Reviews"
  def __str__(self):
    return self.text
  def created_at_formatted(self):
    return timesince(self.created_at)






