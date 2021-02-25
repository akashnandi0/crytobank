import self as self
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views.generic.base import View
from django.contrib.auth import update_session_auth_hash
from profiles.models import createProfileModel, accountInfoModel
from .forms import RegistrationForm
from django.views.generic import CreateView, TemplateView, FormView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class LoginView(FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('welcomeuser')
#     template_name = 'accounts/login.html'


class LoginView(LoginView):
    def get(self, request):
        return render(request, 'accounts/login.html', {'form': AuthenticationForm})

    def post(self, request, username=None):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )

            if user is None:
                return render(
                    request,
                    'accounts/signup.html',
                    {'form': form, 'invalid_creds': True}
                )
            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'accounts/login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)
            return redirect(reverse('welcomeuser'))
        return render(
            request,
            'accounts/login.html',
            {'form': form, 'invalid_creds': True,'username':username}
        )


class HomeView(LoginRequiredMixin, View):
    template_name = 'accounts/welcomeuser.html'
    # template_name = 'base_layout2.html'

    def get(self, request):
        context = {}
        try:
            uid = createProfileModel.objects.get(user=request.user).id
            # print(uid, type(uid))
        except:
            uid = None
            # uid1 = None
        context = {'uid': uid}
        return render(request, 'accounts/welcomeuser.html', context)
        # return render(request, 'base_layout2.html', context)

@login_required
def userpage(request):
    template = loader.get_template("accounts/welcomeuser.html")
    return HttpResponse(template.render({}, request))

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')

#
# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect("logout")
