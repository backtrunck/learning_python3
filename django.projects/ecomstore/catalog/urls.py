#from django.conf.urls.defaults import * 
from django.urls import re_path
from catalog import views
urlpatterns = [
    re_path(r'', views.index,{'template_name':'catalog/index.html'}),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$',views.show_category,{'template_name':'catalog/category.html'}),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$',views.show_product,{'template_name':'catalog/product.html'}),]


