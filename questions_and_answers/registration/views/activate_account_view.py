from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from registration.tokens import account_activation_token

# Activates accounts for users that have completed email-verification for
# sign up. It also adds the user to the group of customers.
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()

        login(request, user)
        return redirect('questions')
    else:
        return render(request, 'account_activation_invalid.html')
