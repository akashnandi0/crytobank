from django.urls import path
from profiles.views import accountsettings
from profiles.views import CreateProfile,success,UpdateprofileView,Deleteprofile,ViewaccountView, ViewprofileView,ViewProfile,change_password, generateaccno, transactions

urlpatterns = [
    path("createprofile/",CreateProfile.as_view(),name="createprofile"),
    path("updateprofile/<int:pk>/", UpdateprofileView.as_view(), name="updateprofile"),
    path("viewprofile/<int:pk>/", ViewprofileView.as_view(), name="viewprofile"),
    path("viewaccount/<int:pk>/", ViewaccountView, name="viewaccount"),
    # path("viewprofile/<int:pk>", ViewProfile, name="viewprofile"),
    path("success/",success,name="success"),
    path("deleteaccount/<slug:pk>/",Deleteprofile.as_view(),name="deleteaccount"),
    path('changepassword/', change_password, name='change_password'),
    path('accountsettings/',accountsettings,name='accountsettings'),
    path('generateaccno/',generateaccno,name='generateaccno'),
    path('transactions/',transactions,name='transactions'),

]