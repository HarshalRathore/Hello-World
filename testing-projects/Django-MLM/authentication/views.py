from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from authentication.models import Profile
from binary_plan.models import create_user, BinaryUserInstence
from authentication.utils import generate_user_id
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        otp = request.POST.get('otp', None)
        login_type = request.POST.get('login_type', None)

        if login_type == 'phone':
            user = Profile.objects.filter(phone_number=phone_number)[0]

            if user is not None:
                if not otp:
                    message_sid = user.send_otp()
                    print("Message SID: ", message_sid)
                    return render(request, 'authentication/login.html', {'phone_number': phone_number, 'otp_field': True})
                if otp:
                    if user.verify_otp(otp):
                        user = authenticate(request, phone_number=phone_number, otp=otp)
                        auth_login(request, user)
                        # Redirect to a success page
                        return redirect('binary-dashboard')
                    error_message = 'OTP expired'
                    return render(request, 'authentication/login.html', {'error_message': error_message, 'phone_number': phone_number, 'otp_field': True})    
            else:
                # Display an error message or handle authentication failure
                error_message = 'Invalid credentials. Please try again.'
                return render(request, 'authentication/login.html', {'error_message': error_message, 'phone_number': phone_number, 'otp_field': False})
        
        elif login_type == 'username':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(request, user_id=username, password=password)

            if user is not None:
                auth_login(request, user)
                # Redirect to a success page
                return redirect('binary-dashboard')
            
            else:
                # Display an error message or handle authentication failure
                error_message = 'Invalid credentials. Please try again.'
                return render(request, 'authentication/login.html', {'error_message': error_message, 'phone_number': '', 'otp_field': False})
    
    else:
        return render(request, 'authentication/login.html', {'phone_number': '', 'otp_field': False})

def register(request):  
    if request.method == 'POST':
        #Handle registration form submission
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        country = request.POST.get('country', None)
        username_referral = request.POST.get('username_referral', None)
        password = request.POST.get('password', None)
        user_id = generate_user_id()
        
        profile = Profile(user_id=f'{first_name}-{user_id}', first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, country=country, password=make_password(password))
        
        if not username_referral:
            profile._referral_user_id = None
            profile.save()
        else:
            username_referral = Profile.objects.filter(user_id=username_referral)

            if username_referral is None:
                error_message = 'Invalid referral username.'
                return render(request, 'authentication/register.html', {'error_message': error_message})

            referral_user_id = BinaryUserInstence.objects.filter(user=username_referral.first()).first()
            profile._referral_user_id = referral_user_id
            profile.save()

        return redirect('login')
    
    return render(request, 'authentication/register.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # So that the user doesn't have to login again
            messages.success(request, 'Your password has been successfully changed.')
            return redirect('change-password')
        else:
            messages.error(request, 'Please correct the errors below and submit it again.')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'authentication/changePassword.html', {'form': form})


# Password reset view
class MyPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    # email_template_name = 'password_reset_email.html'

# Password reset done view
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'
    
# Password reset confirmation view
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

# Password reset complete view
class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'