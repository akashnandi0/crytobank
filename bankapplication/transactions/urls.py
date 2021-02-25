from django.urls import path
from transactions.views import transferamount, depositamount, withdrawamount, accountActivity, balancecheck
urlpatterns = [
    path('transferamount/',transferamount,name='transferamount'),
    path('depositamount/',depositamount,name='depositamount'),
    path('withdrawamount/',withdrawamount,name='withdrawamount'),
    path('balance/<int:pk>',balancecheck.as_view(),name='balanceenquiry'),
    path('accountactivity/<int:pk>', accountActivity.as_view(), name='accountactivity')
]