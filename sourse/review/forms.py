from django import forms

from review.models import Product, Recall


class FindForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Найти")



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'picture']



class RecallForm(forms.ModelForm):
    class Meta:
        model = Recall
        fields = ["sms", "rate", 'moderate']

