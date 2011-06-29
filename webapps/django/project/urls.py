from django.conf.urls.defaults import *
from django.contrib import admin

from shop import urls as shop_urls
from shop_simplevariations import urls as simplevariations_urls


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^shop/cart/', include(simplevariations_urls)),
    (r'^shop/', include(shop_urls)),
)
