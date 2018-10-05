from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup", views.signup_view.signup, name="signup"),
    path("account_activation_sent", views.account_activation_sent_view.account_activation_sent, name="account_activation_sent"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_account_view.activate, name='activate'),
    path("profile/<int:pk>/", views.update_user_profile_view.update_user_profile, name="profile_detail"),
]
