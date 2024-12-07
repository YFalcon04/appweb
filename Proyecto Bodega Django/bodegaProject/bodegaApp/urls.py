from django.urls import path

from bodegaApp.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
    ]