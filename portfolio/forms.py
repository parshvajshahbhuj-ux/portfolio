from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Your Name",
                "autocomplete": "name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "your@email.com",
                "autocomplete": "email",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-input",
                "placeholder": "Tell me about your project or opportunity...",
                "rows": 5,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters.")
        return message
