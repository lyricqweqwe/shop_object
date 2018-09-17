from django.shortcuts import render


from  django.http import  HttpResponse

from apps.shouye.models import *


def index(request):
    #获取导航菜单数据
    navigation = Navigation.objects.all()
    #分类菜单数据
    #三个表 category -->(一对多)  sub_menu-->(一对多)  sub_menu2
    categories=Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()

    #轮播图数据
    banner = Banner.objects.all()

    return  render(request, 'index.html', {'navigation':navigation,'categories':categories,'banner':banner})