from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class BookShop(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 300)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    genre = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    year = models.DateField(auto_now_add = False, auto_now = False)
    date = models.DateField(auto_now_add = True)

# Create your models here.
