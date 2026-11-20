from django import forms


class ContactMessageForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={"autocomplete": "name", "placeholder": "Tu nombre"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "tunombre@correo.com"}),
    )
    subject = forms.CharField(
        max_length=160,
        widget=forms.TextInput(attrs={"placeholder": "¿Sobre qué quieres consultar?"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Escribe aquí tu pregunta o mensaje..."}),
    )
