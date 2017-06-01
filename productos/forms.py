
from django.forms.models import modelformset_factory
from django import forms
from .models import *

# class VariationInventoryForm(forms.ModelForm):
# 	class Meta:
# 		model = Variation
# 		fields = (
# 			"nombre",
# 			"precio",
# 			"sale_price",
# 			"inventorio",
# 			"activo",
# 		)
# VariationInventoryFormSet = modelformset_factory(Variation, form = VariationInventoryForm, extra = 0)
class CrearProductoForm(forms.ModelForm):
	#contenido = forms.CharField(widget=PagedownWidget(show_preview=False))
	#ingrediente = forms.DateField(widget = forms.SelectDateWidget)
	class Meta:
		model = ProductoIngrediente
		fields = [
			"producto",
			"ingrediente",
			"cantidad",
			"unidad",
			]
#CrearProductoFormSet = modelformset_factory(ProductoIngrediente, form = CrearProductoForm, extra = 0)		