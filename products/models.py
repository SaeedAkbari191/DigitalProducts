from django.db import models


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=100, )
    description = models.TextField(verbose_name="Description", blank=True)
    avatar = models.ImageField(verbose_name="Avatar", blank=True, upload_to="Categories/")
    is_enabled = models.BooleanField(verbose_name='Is Enabled', default=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update At', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Category'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description", blank=True)
    avatar = models.ImageField(verbose_name="Avatar", blank=True, upload_to="Products/")
    is_enabled = models.BooleanField(verbose_name='Is Enabled', default=True)
    category = models.ManyToManyField(Category, verbose_name="Category", blank=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update At', auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'Product'

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=50)
    file = models.FileField(verbose_name="File", upload_to="Files/%Y/%m/%d/")
    is_enabled = models.BooleanField(verbose_name='Is Enabled', default=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update At', auto_now=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        db_table = 'File'

    def __str__(self):
        return self.title
