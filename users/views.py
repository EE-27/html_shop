import random

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"

    def get_success_url(self):
        return reverse('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        send_mail(
            "Confirmation of email",
            "Welcome to our website!",
            settings.EMAIL_HOST_USER,
            [user.email]

        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:profile')


def generate_new_password(request):
    new_password = ''.join([str(int(random.random() * 10)) for _ in range(12)])
    send_mail(
        "Change of password",
        f"Your new password is {new_password}",
        settings.EMAIL_HOST_USER,
        [request.user.email]

    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
