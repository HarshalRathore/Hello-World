from django.urls import path
import authentication.views as views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', views.register, name='register'),
    path('change-password/', views.change_password, name='change-password'),
    path('password-reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
