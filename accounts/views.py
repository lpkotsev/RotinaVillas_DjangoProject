from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.models import Group
from .forms import RegisterForm, CustomLoginForm, ProfileForm
from .models import Profile

User = get_user_model()


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])

            user.is_owner = False
            user.save()

            group, _ = Group.objects.get_or_create(name="Users")
            user.groups.add(group)

            login(request, user)
            return redirect("villa-list-page")

        return render(request, "accounts/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = CustomLoginForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile.html"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile.html"   # you are using same template

    def get_object(self):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        user.email = form.cleaned_data.get("email")
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("profile")
