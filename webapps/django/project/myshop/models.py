from django.db import models
from shop.models.productmodel import Product


class Category(models.Model):
    """Master data: Names of categories."""
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Distributor(models.Model):
    """Master data: Information about distributors."""
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class LED(Product):
    """Product class for LED lamps."""
    article_number = models.IntegerField()
    distributor = models.ForeignKey(Distributor)
    image1 = models.ImageField(blank=True, upload_to='myshop_images')
    image2 = models.ImageField(blank=True, upload_to='myshop_images')
    # name - resides in Product base class
    category = models.ForeignKey(Category, blank=False, null=False)
    weight = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return '[%s] %s' % (self.article_number, self.name)
