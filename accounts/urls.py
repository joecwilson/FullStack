from django.urls import path
from .views import SignUpView, ProfileView

app_name = 'account'
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
