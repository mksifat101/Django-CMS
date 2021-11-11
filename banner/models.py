from django.db import models


class HomeBanner1(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='home_banner1')
    link = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HomeBanner2(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='home_banner1')
    link = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
