from django.urls import reverse_lazy
from django.views.generic import (CreateView, TemplateView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationModelForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class IndexPageView(TemplateView):
    template_name = 'index.html'


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/user_detail.html'

    def get_object(self, queryset=None):
        print(self.request.user and self.request.user.has_perm("users.can_get_name"))
        if self.request.user.has_perm("users.can_get_name"):
            return self.request.user


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registration/user_detail.html"

    def get_object(self, queryset=None):
        return self.request.user




