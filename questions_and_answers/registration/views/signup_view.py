from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from registration.forms import SignUpForm
from registration.tokens import account_activation_token

# Creates a new user. Only customer users are created. Admin or staff users, are
# created by another admin or super user through the admin site or the admin
# portion of this site.
def signup(request):
    """Create a new unactivated user in the db for a potential new user."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # This is needed to force the user to rely on the email
            # confirmation. Otherwise, the user can log in without the
            # confirmation email.
            user.is_active = False
            # user_name = f"{user.first_name}_{user.last_name}"
            # Creates new user object in the database.
            user.save()

            # Load the profile instance created by the signal
            # Needed to save the profile details of the user.
            user.refresh_from_db()
            # Save again, to save the new changes made to the user's profile
            user.save()

            # Without this the user will not belong to any group.
            # Newly signed up users can only be customers. Otherwise, they have
            # to have an account created to them by the admin/staff manually.
            group = Group.objects.get(name="Inquirers")
            group.user_set.add(user)

            current_site = get_current_site(request)
            subject = 'Activate Your Questions & Answers Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect("account_activation_sent")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
