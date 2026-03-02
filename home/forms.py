from django import forms
from .models import Item, StorageSpace

class ItemForm(forms.ModelForm):
    storage_space = forms.ModelChoiceField(
        queryset=StorageSpace.objects.filter(is_filled=False),
        label="Available Storage Space",
        empty_label="Select free storage space",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Item
        fields = ['storage_space', 'name', 'sku', 'quantity', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'sku': forms.TextInput(attrs={'class': 'form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'min': 1}),
            'category': forms.TextInput(attrs={'class': 'form-input'}),
        }
