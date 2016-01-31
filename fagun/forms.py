from django import forms


class MailForm(forms.Form):
    user_email = forms.EmailField(
        label="Tölvupóstfang",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )