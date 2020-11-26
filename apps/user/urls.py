from django.urls import path

from apps.user.views import (
    UserRegistrationView, IndexPageView,
    CabinetView)

app_name = "users"

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name="register"),
    path('accounts/cabinet/', CabinetView.as_view(), name='profile'),
    path('', IndexPageView.as_view(), name='index'),

]