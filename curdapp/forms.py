from django import forms

class CreateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product id",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product id',
                'class': 'form-control'
            }
        )
    )

    product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Name',
                'class': 'form-control'
            }
        )
    )

    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )

    product_color = forms.CharField(
        label="Enter Product Color",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Color',
                'class': 'form-control'
            }
        )
    )

    product_class = forms.CharField(
        label="Enter The Product Class",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product class',
                'class': 'form-control'
            }
        )
    )

    customer_name = forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Customer Name',
                'class': 'form-control'
            }
        )
    )

    customer_mobile = forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )

    customer_email = forms.EmailField(
        label="Enter Customer Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Customer Email',
                'class': 'form-control'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product id",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product id',
                'class': 'form-control'
            }
        )
    )

    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product id",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product id',
                'class': 'form-control'
            }
        )
    )



