from django.db import models
from django.template.defaultfilters import  slugify
from django.shortcuts import reverse
# Create your models here.
class Base_Model(models.Model):
    date_add = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract =True

class Category(Base_Model):
    name = models.CharField(max_length=200,unique=True)

    def get_absolute_url(self):
        return reverse("category_page")
    

    def __str__(self):
        return self.name
    
    class Mata:
        verbose_name_plural ='categories'

class Sub_Category(Base_Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_categories')
    name = models.CharField(max_length=200)

     # create a new slug
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category} : {self.name}'
    
    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

class Product(Base_Model):
    category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=100)
    image = models.FileField(upload_to='images/%Y/%m/%d/')
    price=models.DecimalField(decimal_places=2,max_digits=20)
    description = models.TextField(blank=True, null=True)
    is_available= models.BooleanField(default=True)
    slug = models.SlugField(unique=True,editable=False,null=True,blank=True)


    # create a new slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return f'{self.name}: {self.category}'