from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from profiles.models import accountInfoModel
from transactions.models import Transferdetails
from django.contrib import messages
from transactions.forms import TransferAmountForm, DepositAmountForm, WithdrawAmountForm, BalanceCheckForm
from django.contrib.auth.decorators import login_required


@login_required
def transferamount(request):
    form = TransferAmountForm()
    # context = {}
    # context["form"] = form
    context = {"form": form}
    if request.method == "POST":
        form = TransferAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            account_number = form.cleaned_data.get("account_number")
            try:
                object = accountInfoModel.objects.get(mpin=mpin)
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

            # form.save()
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
                object = accountInfoModel.objects.get(mpin=mpin)
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
                object = accountInfoModel.objects.get(mpin=mpin)

                bal = object.balance - amount
                object.balance = bal
                object.save()



            except Exception:
                context["form"] = form
                return render(request, "transactions/depositwithdraw.html", context)

            # form.save()
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/depositwithdraw.html", context)

    return render(request, "transactions/depositwithdraw.html", context)


# @login_required
# def balance(request):
#     form = BalanceCheckForm()
#     context = {}
#     context["form"] = form
#     if (request.method == "POST"):
#         form = BalanceCheckForm(request.POST)
#         if form.is_valid():
#             mpin = form.cleaned_data.get("mpin")
#             try:
#
#                 object = accountInfoModel.objects.get(mpin=mpin)
#                 context["balance"] = object.balance
#                 print(object.balance)
#
#                 return render(request, "transactions/checkbalance.html", context)
#             except Exception as e:
#                 context["form"] = form
#                 return render(request, "transactions/checkbalance.html", context)
#
#     return render(request, "transactions/checkbalance.html", context)

class balancecheck(LoginRequiredMixin, DetailView):
    model = accountInfoModel
    fields = ["balance"]
    template_name = 'transactions/checkbalance.html'


# @login_required
# def accountActivity(request):
#     form = BalanceCheckForm()
#     context = {}
#     context["form"] = form
#     if (request.method == "POST"):
#         form = BalanceCheckForm(request.POST)
#         if form.is_valid():
#             mpin = form.cleaned_data.get("mpin")
#
#             trans = Transferdetails.objects.filter(mpin=mpin)
#
#             context["transaction"] = trans
#             return render(request, "transactions/accountactivity.html", context)
#
#     return render(request, "transactions/accountactivity.html", context)


class accountActivity(LoginRequiredMixin, ListView):
    model = Transferdetails
    # forms=TransferForm()
    fields = ["account_number", "amount", "date"]
    template_name = "transactions/accountactivity1.html"

    def get_initial(self):
        return {'user': self.request.user}

    def get_queryset(self):
        mpin = accountInfoModel.objects.get(username=self.request.user).mpin
        return Transferdetails.objects.filter(mpin=mpin)
        # trans = transferamount.objects.filter(mpin=mpin)
        # context["transaction"] = trans
        # return render("transactions/accountactivity1.html")
