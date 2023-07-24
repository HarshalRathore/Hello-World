# forms.py
from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=20)
    address = forms.CharField(label='Address', widget=forms.Textarea)
    country = forms.CharField(label='Country', max_length=100)
    zipcode = forms.CharField(label='Zip Code', max_length=10)

    def __init__(self, *args, **kwargs):
        user_details = kwargs.pop('user_details', None)
        super(CheckoutForm, self).__init__(*args, **kwargs)

        if user_details:
            self.fields['name'].initial = user_details.get('first_name', '')
            self.fields['email'].initial = user_details.get('email', '')
            self.fields['phone'].initial = user_details.get('phone_number', '')
            self.fields['address'].initial = "\n".join(user_details.get('address', []))
            self.fields['country'].initial = user_details.get('country', '')
            self.fields['zipcode'].initial = user_details.get('zip_code', '')
