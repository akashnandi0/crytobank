# bankapplication
Assignment - Bank System
Name - Crypto Bank
App list:
  1. accounts(handling user account)
  2. profiles(handling customer profiles)
  3. transactions(handling customer transactions)

Duties of accounts app:
-uses registration form that inherits UserCreationForm
-create account
-login to account
-homepage of user
-reset password using email verification link

Duties of profiles app:
-setting the account - generating account number, changing password etc
-create,delete,update,view profile and accounts
-list of transacations possible (further connects to transaction app)
-contains createprofilemodel(inherited from User) and accountinfomodel(inherited from User)
-contains createprofileform
-contains LoginRequiredMixin process

Duties of transactions app:
-transferdetails model to hold the data of all transfers done
-deposit,transfer,withdraw and check balance in the bank account
-contains only function based views

It also contains a static and template folders with images, html files, css files inside.
