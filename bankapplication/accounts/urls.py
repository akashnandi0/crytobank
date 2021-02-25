from django.urls import path
from django.contrib.auth import views as auth_views
from bankapplication import settings
from .views import SignUpView, LoginView, logout, HomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('welcomeuser/', HomeView.as_view(), name='welcomeuser'),
    path('logout/', logout, name='logout'),
    # Forgot Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             subject_template_name='accounts/password_reset_subject.txt',
             # email_template_name='accounts/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
