from django import forms
from home.models import btech, mtechcs, mtechai, pgd, mscdf


class btechforms(forms.ModelForm):
    class Meta:
        model = btech
        #        fields="__all__" except ('')
        fields = ('mobile', 'aadhar', 'name', 'email', 'dob', 'percent', 'percentile', 'pincode',)
        # fields=('mobile',)


class mtechcsforms(forms.ModelForm):
    class Meta:
        model = mtechcs
        #        fields="__all__" except ('')
        fields = ('mobile', 'aadhar', 'name', 'email', 'dob', 'cgpa', 'gatescore', 'pincode')


class mtechaiforms(forms.ModelForm):
    class Meta:
        model = mtechai
        #        fields="__all__" except ('')
        # fields=('mobile','aadhar','name','email','mobile','dob','gender','cgpa','gatescore','category','pincode')
        # fields=('mobile','aadhar','name','email',)
        fields = ('mobile', 'aadhar', 'name', 'email', 'dob', 'cgpa', 'gatescore', 'pincode')


class MScDfForms(forms.ModelForm):
    class Meta:
        model = mscdf
        #        fields="__all__" except ('')
        # fields=('mobile','aadhar','name','email','mobile','dob','gender','cgpa','gatescore','category','pincode')
        # fields=('mobile','aadhar','name','email',)
        fields = ('mobile', 'aadhar', 'name', 'email', 'dob', 'cgpa', 'pincode')


class pgdforms(forms.ModelForm):
    class Meta:
        model = pgd
        #        fields="__all__" except ('')
        # fields=('mobile','aadhar','name','email','mobile','dob','gender','cgpa','gatescore','category','pincode')
        # fields=('mobile','aadhar','name','email',)
        # fields=('mobile','aadhar','name','email','dob','gender','cgpa','category','pincode')
        fields = ('mobile', 'aadhar', 'name', 'email', 'dob', 'cgpa', 'pincode')
        # fields=('mobile')
