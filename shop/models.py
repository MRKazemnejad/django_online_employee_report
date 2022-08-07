from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator



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


class Order(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='orders')
    paid=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    discount=models.IntegerField(null=True,blank=True,default=None)

    def get_total_price(self):
        total_price=sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price=(self.discount/100)*total_price
            return (total_price-discount_price)
        return total_price

    class Meta:
        ordering=('paid',)

    def __str__(self):
        return self.user


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()


    def __str__(self):
        return f"{self.order}"

    def get_cost(self):
        return self.quantity * self.price


class Coupon(models.Model):
    code=models.CharField(max_length=30,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    active=models.BooleanField()
    discount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(90)])

    def __str__(self):
        return self.code