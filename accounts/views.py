from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View  
from . import forms
from django.shortcuts import redirect


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # Redirect to the homepage or another page
