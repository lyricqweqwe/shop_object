from django.contrib import admin
from django.conf.urls import url,include

from shouye import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',views.index),
    url('shouye/', include('apps.shouye.urls')),
    url('account/', include('apps.account.urls')),
    url('order/', include('apps.order.urls')),
    url('pay/', include('apps.pay.urls')),
    url('shop/', include('apps.shop.urls')),
    url('shopcard/', include('apps.shopcard.urls')),
    url('fenlei/', include('apps.fenlei.urls')),

]
