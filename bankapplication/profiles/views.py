from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from profiles.forms import createProfileForm
from django.urls import reverse_lazy
from profiles.models import createProfileModel, accountInfoModel
from django.contrib import messages, auth
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class CreateProfile(LoginRequiredMixin, CreateView):
    form_class = createProfileForm
    success_url = reverse_lazy('accountsettings')
    template_name = "profiles/createprofile.html"

    def get_initial(self):
        return {'user': self.request.user}


@login_required
def success(request):
    return render(request, "profiles/success.html")


#
class UpdateprofileView(LoginRequiredMixin, UpdateView):
    # form_class = updateProfileForm
    model = createProfileModel
    fields = ["age", "sex", "marital_status", "date_of_birth", "phone_number", "alternate_phone_number", "address",
              "city", "state", "pin_code"]
    # form_class = createProfileForm
    success_url = reverse_lazy('welcomeuser')
    template_name = "profiles/updateprofile.html"


class ViewprofileView(LoginRequiredMixin, DetailView):
    model = createProfileModel
    fields = "__all__"
    # form_class = createProfileForm
    success_url = reverse_lazy('welcomeuser')
    template_name = "profiles/viewprofile.html"


@login_required
def ViewaccountView(request, pk):
    st = accountInfoModel.objects.get(id=pk)
    return render(request, 'profiles/viewaccount.html', {'st': st})


@login_required
def ViewProfile(request, pk):
    st = createProfileModel.objects.get(id=pk)
    return render(request, 'profiles/viewprofile.html', {'st': st})


class Deleteprofile(LoginRequiredMixin, DeleteView):
    model = User
    fields = "__all__"
    success_url = reverse_lazy('myhome')
    template_name = "profiles/deleteprofile.html"


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            auth.logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {
        'form': form
    })


def genaccno():
    # return a 11 digit random number
    return int(random.uniform(10000000000, 99999999999))


def genpin():
    # return a 4 digit random number
    return int(random.uniform(1000, 9999))


@login_required
def accountsettings(request):
    return render(request, "profiles/accountsettings.html")


@login_required
def generateaccno(request):
    try:
        curr_user = accountInfoModel.objects.get(username=request.user)  # getting details of current user
        uid1 = accountInfoModel.objects.get(username_id=request.user).id
    except:
        # if no details exist (new user), create new details
        uid1 = None
        curr_user = accountInfoModel()
        curr_user.account_number = genaccno()  # random account number for every new user
        curr_user.mpin = genpin()  # random pin for every new user
        curr_user.balance = 1000
        curr_user.acctype = "Savings"
        curr_user.username = request.user
        curr_user.save()
    return render(request, "profiles/generatesuccess.html", {"curr_user": curr_user})


@login_required
def transactions(request):
    return render(request, "profiles/transactions.html")
