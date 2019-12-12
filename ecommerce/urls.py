"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from core.views import *
from core import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', Index.as_view(), name='index'),
    # url(r'^contato/$', Contact.as_view(), name='contato'),
    # url(r'^produto/$', Product.as_view(), name='produto'),
    # url(r'^produtos/$', ProductList.as_view(), name='produto_listar'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contato'),
    url(r'^produto/$', views.product, name='produto'),
    url(r'^produtos/$', views.productList, name='produto_listar'),
]
