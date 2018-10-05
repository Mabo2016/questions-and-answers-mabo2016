from django.forms import ModelForm
from registration.models import User

class UserDetailModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
