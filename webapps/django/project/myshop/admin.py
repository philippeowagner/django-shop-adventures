from django.contrib import admin

from shop_simplecategories.admin import ProductWithCategoryForm

from myshop import models as shop_models


class LEDProductForm(ProductWithCategoryForm):
    class Meta(object):
        model = shop_models.LED


class LEDAdmin(admin.ModelAdmin):
    form = LEDProductForm
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(shop_models.Distributor)
admin.site.register(shop_models.LED, LEDAdmin)
