from django import forms

class AddPerson(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name",
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name",
        })
    )
    phone_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Phone Number",
        })
    )


