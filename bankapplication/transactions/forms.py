from django import forms
from django.forms import ModelForm
from transactions.models import Transferdetails
from profiles.models import accountInfoModel, createProfileModel


class TransferAmountForm(ModelForm):
    class Meta:
        model = Transferdetails
        fields = ["account_number","amount","mpin"]
        labels = {
            "amount": "Enter Transfer Amount",
            "mpin": "Enter Unique Pin(mpin)",
            "account_number": "Enter Destination Account Number"
        }
        widgets = {
            "mpin": forms.PasswordInput(),

        }

    def clean(self):
        cleaned_data = super().clean()
        account_number = cleaned_data.get("account_number")
        amount = cleaned_data.get("amount")
        mpin = cleaned_data.get("mpin")
        print(mpin, ",", account_number, ",", amount)
        try:
            object = accountInfoModel.objects.get(mpin=mpin)
            if (object):

                # for checking sufficent balance
                if (object.balance < amount):
                    msg = "insufficent amount"
                    self.add_error("amount", msg)
                pass
        except:
            msg = "you have provided invalid mpin"
            self.add_error("mpin", msg)
        # for account validation
        try:
            object = accountInfoModel.objects.get(account_number=account_number)
            if (object):
                pass
        except:
            msg = "you have provided invalid account number"
            self.add_error("account_number", msg)


class WithdrawAmountForm(ModelForm):
    class Meta:
        model = Transferdetails
        fields = ["amount", "mpin"]
        labels = {
            "amount": "Enter Amount: ",
            "mpin": "Enter Unique Pin(mpin): "
        }
        widgets = {
            "mpin": forms.PasswordInput(),

        }

    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get("mpin")
        account_number = cleaned_data.get("account_number")
        amount = cleaned_data.get("amount")
        print(mpin, ",", amount)
        try:
            object = accountInfoModel.objects.get(mpin=mpin)
            if (object):

                # for checking sufficent balance
                if (object.balance < amount):
                    msg = "insufficent amount"
                    self.add_error("amount", msg)
                pass

        except:
            msg = "you have provided invalid mpin"
            self.add_error("mpin", msg)


class DepositAmountForm(ModelForm):
    class Meta:
        model = Transferdetails
        fields = ["amount", "mpin"]
        labels = {
            "amount": "Enter Amount: ",
            "mpin": "Enter Unique Pin(mpin): "
        }
        widgets = {
            "mpin": forms.PasswordInput(),

        }

    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get("mpin")
        account_number = cleaned_data.get("account_number")
        amount = cleaned_data.get("amount")
        print(mpin, ",", amount)
        try:
            object = accountInfoModel.objects.get(mpin=mpin)
            if (object):

                # for checking sufficent balance
                if (object.balance < amount):
                    pass

        except:
            msg = "you have provided invalid mpin"
            self.add_error("mpin", msg)


class BalanceCheckForm(ModelForm):
    class Meta:
        model = Transferdetails
        fields = ["mpin"]
        labels = {
            "mpin": "Enter Unique Pin(mpin): "
        }
        widgets = {
            "mpin": forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get("mpin")
        print(mpin)
        try:
            object = accountInfoModel.objects.get(mpin=mpin)
            if (object):

                # for checking balance
                if (object.balance):
                    pass
        except:
            msg = "you have provided invalid mpin"
            self.add_error("mpin", msg)
