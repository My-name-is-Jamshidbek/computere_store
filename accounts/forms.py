from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'republic', 'region', 'district_or_city',
                  'street', 'house_number', 'apartment_number', 'postal_code',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'republic', 'region', 'district_or_city',
                  'street', 'house_number', 'apartment_number', 'postal_code',)