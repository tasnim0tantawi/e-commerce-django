from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    # db index is used to speed up the search in the database, it is used for fields that are frequently searched.
    name = models.CharField(max_length=250, db_index=True)
    # slug is a short label that contains only letters, numbers, underscores or hyphens. They are used in URLs.
    # for example: https://www.example.com/electronics/
    slug = models.SlugField(max_length=250, unique=True)

    # Define meta data for the model
    class Meta:
        # Because the plural of category is categories, we need to define it here.
        # So Django will use this instead of categorys (django will add 's' to the model name)
        verbose_name_plural = 'categories'

    def __str__(self):
        # This is used to display the name of the category in the admin panel instead of 'Category object (1)'.
        # For example: 'Electronics'
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Product(models.Model):
    # FK

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    # blank=True means that this field is optional
    description = models.TextField(blank=True)
    # slug is unique for each product
    slug = models.SlugField(max_length=250)
    # DecimalField is used for decimal numbers
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse() function is used to return the url as a string
        # product-info is the name of the url in urls.py
        # args is a list of arguments that will be passed to the url (in this case, the slug)
        return reverse('product-info', args=[self.slug])




