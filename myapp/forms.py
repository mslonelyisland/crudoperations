from django import forms
from myapp.models import Orders
from django.contrib.auth.forms import AuthenticationForm

class OrdersForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
        ('Shipped', 'Shipped'),
    )

    PAID_CHOICES = (
        ('Partial Payment', 'Partial Payment'),
        ('Full Payment', 'Full Payment'),
    )

    PAYMENT_CHOICES = (
        ('Paypal', 'Paypal'),
        ('Gcash', 'Gcash'),
        ('Paymaya', 'Paymaya'),
        ('BankTransfer', 'Bank Transfer'),
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    paid = forms.ChoiceField(
        choices=PAID_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    payment = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Orders
        fields = ['name', 'email', 'status', 'phone', 'address', 'notes', 'figures', 'paid', 'payment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
            'figures': forms.NumberInput(attrs={'class': 'form-control'}),
            'paid': forms.TextInput(attrs={'class': 'form-control'}),
            'payment': forms.TextInput(attrs={'class': 'form-control'}),
        }


    # class LoginForm(AuthenticationForm):{

    # }
