
from django.contrib import admin
from django.urls import path
from .views import homeview,papers
from users.views import register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# '' home template

# login for login template

# logout for logout template

# register for registtering new user

# papers for research papers page

# password_change/done for Passwordchangedoneview(predefined view) when password change done

# password_change/ for Passwordchangeview(predefined view) for updating passwords

# password_reset/done for Passwordresetcompleteview(predefined view) when reset password done

# reset/<token> for Passwordresetconfirmview(predefined view) for new password reset link

# password_reset/ for Passwordresetview(predefined view) for filling out emailID for resetting password


# these urls are serving different views
urlpatterns = [
    path('',homeview,name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/',register,name='register'),
    path('papers/',papers.as_view(),name='papers'),
    
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'
        ), name='password_change_done'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html'
        ), name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_done.html'
        ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
     name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
        ), name='password_reset_complete'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)