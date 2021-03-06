from django import forms

class ropa_forms(forms.Form):
    ropa_name = forms.CharField(max_length=200)
    ropa_color = forms.CharField(max_length=100)
    ropa_marca = forms.CharField(max_length=100)
    ropa_precio = forms.FloatField()
    ropa_imagen = forms.ImageField()

class championes_forms(forms.Form):
    championes_name = forms.CharField(max_length=200)
    championes_color = forms.CharField(max_length=100)
    championes_marca = forms.CharField(max_length=100)
    championes_precio = forms.FloatField()
    championes_imagen = forms.ImageField()
    
class accesorios_forms(forms.Form):
    accesorio_name = forms.CharField(max_length=200)
    accesorio_tipo = forms.CharField(max_length=100)
    accesorio_marca = forms.CharField(max_length=100)
    accesorio_precio = forms.FloatField()
    accesorio_imagen = forms.ImageField()

    
