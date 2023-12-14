
from django import forms

from catalog.models import Product, Version


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

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


