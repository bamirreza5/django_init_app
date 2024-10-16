from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModelManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted = False)
    

class BaseModel(models.Model):
    deleted = models.BooleanField(null=True , blank= True , editable= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManger()
    class Meta : 
        abstract = True 
class category(BaseModel):
    title = models.CharField(max_length=100)
    deleted = models.BooleanField(null=True,blank=True)
    def __str__(self):
        return self.title
    
class Product(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image =models.ImageField()
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    # created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

class Cart(BaseModel):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Order(BaseModel):
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(null=True)
    # created_at = models.DateField(auto_now_add=True)

class OrderProduct(BaseModel):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True)
    quantity = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    # created_at = models.DateField(auto_now_add=True)

class PaymentLog(models.Model):
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    status = models.CharField(max_length=100)
    error_code = models.CharField(max_length=100)
