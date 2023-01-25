from django import forms

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'picture']


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']


class ModeratorReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'is_moderated']
