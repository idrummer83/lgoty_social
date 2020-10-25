from .models import Subscribe, FeedBack, Agency

from django.core.validators import validate_email, validate_integer
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class FeedBackForm(ModelForm):

    class Meta:
        model = FeedBack
        fields = ['fio', 'message', 'theme', 'phone', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise ValidationError('Введите правильное поле с email')
        return email

    def validate_integer(self):
        phone = self.cleaned_data['phone']
        if validate_integer(phone):
            raise ValidationError('Введите правильное поле с phone')
        return phone


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'phone', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            raise ValidationError('Введите правильное поле с email')
        return email

    def validate_integer(self):
        phone = self.cleaned_data['phone']
        if validate_integer(phone):
            raise ValidationError('Введите правильное поле с phone')
        return phone


class AgencyForm(ModelForm):

    class Meta:
        model = Agency
        fields = ['building']
