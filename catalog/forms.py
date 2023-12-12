"""
Assignment 1 Continue working with the project from the previous homework assignment.
For the product model, implement the CRUD mechanism using the django.forms module .

Conditions for users:

 can create new products; cannot upload forbidden products to the platform.
 To exclude uploading forbidden products, implement validation of the product name and
 description in such a way that it is impossible to add the
 words: casino, cryptocurrency, crypta, exchange, cheap, free, scam, police, radar.
"""
from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        forbidden_words = ["casino", "cryptocurrency", "crypta", "exchange", "cheap", "free", "scam", "police", "radar"]
        for word in forbidden_words:
            if word in str(cleaned_data).lower():
                raise forms.ValidationError(f"Fuck off - no {word}")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        forbidden_words = ["casino", "cryptocurrency", "crypta", "exchange", "cheap", "free", "scam", "police", "radar"]
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Fuck off - no {word}")

        return cleaned_data
