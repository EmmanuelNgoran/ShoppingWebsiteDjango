from django import forms, ModelForm
from shoppingBoard.models import productSpec
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
def size_choice():
    type=productSpec.objects.get(product__sub_category__product_type)

class CartAddProductForm(ModelForm):
    class Meta:
        models=productSpec
        fields=[size,]
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    size=forms.TypedChoiceField(choices=,coerce=string)    
    update = forms.BooleanField(required=False,  initial=False,  widget=forms.HiddenInput)