from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import CategoryListView, CategoryDetailView
urlpatterns = [
    # Examples:
    #url(r'^$', 'newsletter.views.home', name='home'),
    #url(r'^edit/producto/(?P<id_prod>.*)/$','edit_product_view',name= "vista_editar_producto"),
    url(r'^$', CategoryListView.as_view(), name='categorias'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='categoria_detalle'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail', name='producto_detalle_view'),
 ]

