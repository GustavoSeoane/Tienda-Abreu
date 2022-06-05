from django import forms

class ropa_forms(forms.Form):
    ropa_name = forms.CharField(max_length=200)
    ropa_color = forms.CharField(max_length=100)
    ropa_marca = forms.CharField(max_length=100)
    ropa_precio = forms.FloatField()
  
