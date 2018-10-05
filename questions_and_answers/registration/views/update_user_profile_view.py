from django.contrib.auth.models import User
from django.shortcuts import render
from django.forms.models import model_to_dict

from registration.forms import ProfileDetailModelForm, UserDetailModelForm
from registration.models import Profile

def update_user_profile(request, pk):
    """Updates the profile of a user by the user himself or herself"""
    if request.method == "POST":
        # Create a form to edit an existing user
        # Populate the form with the existing user's current details
        user_form_instance = User.objects.get(pk=request.user.id)
        user_form = UserDetailModelForm(request.POST, instance=user_form_instance)
        # Create a form to edit an existing profile
        # Populate the form with the existing profile's current details
        profile_form_instance = Profile.objects.get(pk=pk)
        profile_form = ProfileDetailModelForm(request.POST, instance=profile_form_instance)

        if user_form.is_valid() and profile_form.is_valid():
            # Update the user's details in the database
            user_form.save()
            # Update the profile's details in the database
            profile_form.save()
    else:
        # Create a form to edit an existing user or profile
        # Populate the form with the existing user's current details

        # Get the user's model from the database
        user_form_instance = User.objects.get(pk=request.user.id)
        # Convert its attributes to a dictionary.
        # Needed to display the initial values of the model to the user.
        dictionary = model_to_dict(user_form_instance)
        # Supply the form with the model and its data.
        # The form will actually render all that to the user.
        # So it needs it to create the html.
        user_form = UserDetailModelForm(dictionary)

        # Same as above with user.
        profile_form_instance = Profile.objects.get(pk=pk)
        dictionary = model_to_dict(profile_form_instance)
        profile_form = ProfileDetailModelForm(dictionary)

    return render(request, "user_profile.html", {"user_form": user_form, "profile_form": profile_form})
