from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_category_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    images = models.ImageField(upload_to='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
