from django.db import models


class Category(models.Model):
    """Category Model"""
    category_type = models.CharField(primary_key=True, unique=True, max_length=200, default='')
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    """Size Model"""
    size = models.CharField(max_length=3)

    def __str__(self):
        return self.size


class Theme(models.Model):
    """Product Themes Model"""
    theme = models.CharField(max_length=50)
    sub_theme = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.theme


class Product(models.Model):
    """Product Model"""
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='', related_name='product_category')
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ManyToManyField(Size, related_name='product_size', blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, blank=True, null=True, related_name='product_theme')
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name