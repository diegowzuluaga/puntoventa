from django.contrib import admin

# Register your models here.
from .models import Producto, Ingrediente, Unidad, ProductoImage, Categoria, ProductoCategoria, ProductoIngrediente # ProductoFeatured Variation,

class ProductoImageInLine(admin.TabularInline):
	model = ProductoImage
	extra = 0
	max_num = 10


# class VariationInLine(admin.TabularInline):
# 	model = Variation
# 	extra = 0 #numero de lineas en el formulario de Variation
# 	max_num = 10

class ProductoIngredienteInLine(admin.TabularInline):
	model = ProductoIngrediente
	extra = 0 #numero de lineas en el formulario de Variation
	max_num = 10




class ProductoAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'precio']
	inlines = [
	       ProductoImageInLine,
	       ProductoIngredienteInLine,
	]
	
	class Meta:
		model = Producto

admin.site.register(Producto, ProductoAdmin)
#admin.site.register(ProductImage)
admin.site.register(Categoria)
admin.site.register(ProductoCategoria)
admin.site.register(Unidad)
admin.site.register(Ingrediente)
#admin.site.register(ProductoIngrediente)
#admin.site.register(ProductoFeatured)
#admin.site.register(Variation)
