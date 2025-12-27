# cart/forms.py

from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'quantity-input'}), label="تعداد")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
