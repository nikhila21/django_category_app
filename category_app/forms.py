from django import forms
from .models import Category, SubCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('id', 'categories',)


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('catid', 'subcategory',)
