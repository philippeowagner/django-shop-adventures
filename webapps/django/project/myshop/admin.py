from django.contrib import admin

from myshop import models as shop_models


class LEDAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(shop_models.Category)
admin.site.register(shop_models.Distributor)
admin.site.register(shop_models.LED, LEDAdmin)
