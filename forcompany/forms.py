# -*- coding: utf-8 -*-

from django import forms

from registration.forms import RegistrationForm
from django import forms
from .models import CompanyMasterProfile

class CompanyMasterProfileForm(RegistrationForm):

    company_name = forms.CharField(required=True, label='학원이름(*)',
                                   widget=forms.TextInput(attrs={'placeholder': '매치스튜디오'}),
                                   help_text='is company name')

    local_number = forms.CharField(required=True)

    phone_number = forms.CharField(required=True)

    address = forms.CharField(required=True)

    nearby_station = forms.CharField()

    refund_information = forms.CharField()


    def __init__(self, *args, **kwargs):
        super(CompanyMasterProfileForm, self).__init__(*args, **kwargs)

    # class Meta:
    #     model = CompanyMasterProfile
    #     fields = ('company_name','local_number','phone_number','address','nearby_station','refund_information',)

