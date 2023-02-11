from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    price = models.IntegerField(verbose_name='Price')


