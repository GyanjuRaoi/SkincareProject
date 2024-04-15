from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200)
    productImage = models.ImageField(upload_to='product', blank= True)
    productType = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @classmethod
    def create(cls, name, description, productImage, productType):
        product = cls(name=name, description=description, productImage=productImage, productType=productType)
        product.save()
        return product
    
    def update(self, name=None, description=None, productImage=None, productType=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if productImage:
            self.productImage = productImage
        if productType:
            self.productType = productType
        
        self.save()
    
    def delete(self):
        super().delete()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home_page")
    
    



    
    