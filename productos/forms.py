
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
