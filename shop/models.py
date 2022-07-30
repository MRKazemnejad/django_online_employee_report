from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_name')
    image=models.ImageField(upload_to='products/')
    price=models.IntegerField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)

    class Meta:
        ordering=('name',)


    def __str__(self):
        return f"{self.name}-{self.price}-{self.available}"


