from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.productList, name='produto_listar'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
]