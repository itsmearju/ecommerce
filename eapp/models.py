from django.db import models

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)
    slug= models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug= models.SlugField(max_length=250, unique=True)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='product/%Y/%m/%d', blank=True, null= True)
    stock= models.IntegerField()
    available= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()    
     
    def __str__(self):
        return self.name
    