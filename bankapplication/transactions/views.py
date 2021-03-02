from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from profiles.models import accountInfoModel
from transactions.models import Transferdetails
from django.contrib import messages
from transactions.forms import TransferAmountForm, DepositAmountForm, WithdrawAmountForm
from django.contrib.auth.decorators import login_required


@login_required
def transferamount(request):
    form = TransferAmountForm()
    context = {"form": form}
    if request.method == "POST":
        form = TransferAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            account_number = form.cleaned_data.get("account_number")
            try:
                object = accountInfoModel.objects.get(username=request.user, mpin=mpin)
                object1 = accountInfoModel.objects.get(account_number=account_number)
                bal = object.balance - amount
                bal1 = object1.balance + amount
                object.balance = bal
                object1.balance = bal1
                object.save()
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "transactions/transferamount.html", context)


            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/transferamount.html", context)

    return render(request, "transactions/transferamount.html", context)


@login_required
def depositamount(request):
    form = DepositAmountForm()
    context = {"form": form}
    m = "Credit"
    if request.method == "POST":
        form = DepositAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            messages.success(request, "Deposited Successfully")
            try:
                object = accountInfoModel.objects.get(username=request.user, mpin=mpin)
                bal = object.balance + amount
                object.balance = bal
                object.save()



            except Exception:
                context["form"] = form
                return render(request, "transactions/depositwithdraw.html", context)

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/depositwithdraw.html", context)

    return render(request, "transactions/depositwithdraw.html", context)


@login_required
def withdrawamount(request):
    form = WithdrawAmountForm()
    context = {"form": form}
    if request.method == "POST":
        form = WithdrawAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            try:
                object = accountInfoModel.objects.get(username=request.user, mpin=mpin)

                bal = object.balance - amount
                object.balance = bal
                object.save()



            except Exception:
                context["form"] = form
                return render(request, "transactions/depositwithdraw.html", context)

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/depositwithdraw.html", context)

    return render(request, "transactions/depositwithdraw.html", context)


class balancecheck(LoginRequiredMixin, DetailView):
    model = accountInfoModel
    fields = ["balance"]
    template_name = 'transactions/checkbalance.html'


class accountActivity(LoginRequiredMixin, ListView):
    model = Transferdetails
    fields = ["account_number", "amount", "date"]
    template_name = "transactions/accountactivity1.html"

    def get_initial(self):
        return {'user': self.request.user}

    def get_queryset(self):
        mpin = accountInfoModel.objects.get(username=self.request.user).mpin
        return Transferdetails.objects.filter(mpin=mpin).order_by('-date')[:10]
