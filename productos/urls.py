from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView, ProductListView, imprimir #VariationListView

urlpatterns = [
    # Examples:
    #url(r'^$', 'newsletter.views.home', name='home'),
    #url(r'^edit/producto/(?P<id_prod>.*)/$','edit_product_view',name= "vista_editar_producto"),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='producto_detalle'),
    url(r'^$', ProductListView.as_view(), name='productos'),
    #url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail', name='producto_detalle_view'),
    url(r'^imprimir/$', imprimir, name='imprimir'),
 ]

