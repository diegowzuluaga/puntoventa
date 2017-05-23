from django.contrib import admin

# Register your models here.
from .models import Producto, ProductoImage, Categoria, ProductoCategoria # ProductoFeatured Variation,

class ProductoImageInLine(admin.TabularInline):
	model = ProductoImage
	extra = 0
	max_num = 10


# class VariationInLine(admin.TabularInline):
# 	model = Variation
# 	extra = 0 #numero de lineas en el formulario de Variation
# 	max_num = 10


class ProductoAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'precio']
	inlines = [
	    ProductoImageInLine,
	    #VariationInLine,

	]
	class Meta:
		model = Producto

admin.site.register(Producto, ProductoAdmin)
#admin.site.register(ProductImage)
admin.site.register(Categoria)
admin.site.register(ProductoCategoria)
#admin.site.register(ProductoFeatured)
#admin.site.register(Variation)
