from django import forms


class getData(forms.Form):
    consultancy_name = forms.CharField()
    pay_rate = forms.IntegerField()
    contact_number = forms.IntegerField(required=False)
    contract = forms.ChoiceField(choices=((1,'YES'), (2, 'NO'), ))
    contract_lenght = forms.IntegerField()
    training_fee = forms.IntegerField(required=False)
    relocation = forms.ChoiceField(choices=((1,'YES'), (2, 'NO'), ))
    status = forms.CharField(required=False)
