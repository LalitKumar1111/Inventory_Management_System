from django import forms
from .models import *

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields=['name','email','mobile','address']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class':'form-control'
            })
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields=['deptname','email','mobile','address']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class':'form-control'
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','pcode','category','unit','pricepu','stockinhand','minstacktomaintain']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['catname','catdetails']


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields=['uname']


class POForm(forms.ModelForm):
    class Meta:
        model = PO
        fields=['ponum','podate','supplier','pname','rquantity','uname','priceperunit','amount','deliverystatus','paymentstatus']
        

class SOForm(forms.ModelForm):
    class Meta:
        model = SO
        fields=['sonum','sodate','deptname','username','pname','rquantity','uname','priceperunit','amount','deliverystatus']
        


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields=['deptname','name','email','mobile']

