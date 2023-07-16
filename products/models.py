import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,blank=True)

    def save(self , *args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name



class Ingredient(models.Model):
    ingredients_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,blank=True)

    def save(self , *args,**kwargs):
        self.slug = slugify(self.ingredients_name)
        super(Ingredient,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.ingredients_name



class Product(models.Model):
    category = models.ForeignKey(Category,related_name='main_category',on_delete=models.CASCADE)
    category1 = models.ForeignKey(Category,related_name='category1',blank=True,null=True,on_delete=models.CASCADE)
    category2 = models.ForeignKey(Category,related_name='category2',blank=True,null=True,on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 100)
    costprice = models.IntegerField()
    sellingprice = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=30)
    ingredient1 = models.ForeignKey(Ingredient,related_name='ingredient2',blank=True,null=True,on_delete=models.PROTECT)
    ingredient2 = models.ForeignKey(Ingredient,related_name='ingredient1',blank=True,null=True,on_delete=models.PROTECT)
    ingredient3 = models.ForeignKey(Ingredient,related_name='ingredient3',blank=True,null=True,on_delete=models.PROTECT)
    ingredient4 = models.ForeignKey(Ingredient,related_name='ingredient4',blank=True,null=True,on_delete=models.PROTECT)
    ingredient5 = models.ForeignKey(Ingredient,related_name='ingredient5',blank=True,null=True,on_delete=models.PROTECT)
    ingredient6 = models.ForeignKey(Ingredient,related_name='ingredient6',blank=True,null=True,on_delete=models.PROTECT)
    ingredient7 = models.ForeignKey(Ingredient,related_name='ingredient7',blank=True,null=True,on_delete=models.PROTECT)
    ingredient8 = models.ForeignKey(Ingredient,related_name='ingredient8',blank=True,null=True,on_delete=models.PROTECT)
    ingredient9 = models.ForeignKey(Ingredient,related_name='ingredient9',blank=True,null=True,on_delete=models.PROTECT)


    def __str__(self):
        return self.product_name
    
