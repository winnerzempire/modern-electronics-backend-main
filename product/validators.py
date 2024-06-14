from rest_framework.validators import UniqueValidator
from .models import Category

unique_validator=UniqueValidator(Category.objects.all(), lookup="iexact")