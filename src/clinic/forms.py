from phonenumber_field.formfields import PhoneNumberField

from django import forms
from django.core.validators import RegexValidator

from clinic.models import Review


class ReviewForm(forms.ModelForm):
    phone = PhoneNumberField(
        label='Номер телефона',
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{7,15}$',
                message='Номер телефона необходимо ввести в формате: +XXXXXXXXXXXXX.',
            ),
        ],
        required=False,
    )

    class Meta:
        model = Review
        fields = ('name', 'email', 'phone', 'message', 'rating', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': ''}),
            'email': forms.EmailInput(attrs={'placeholder': ''}),
            'phone': forms.TextInput(attrs={'placeholder': ''}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': ''}),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={'class': 'rating-select'},
            ),
            'image': forms.ClearableFileInput(attrs={'placeholder': ''}),
        }
        labels = {
            'name': 'Ваше имя*',
            'email': 'Почта*',
            'message': 'Сообщение*',
            'rating': 'Оценка*',
            'image': 'Фото',
        }