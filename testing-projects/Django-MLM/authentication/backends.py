from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class OTPBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, otp=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(phone_number=phone_number)
            if user.verify_otp(otp):
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
        
    def user_can_authenticate(self, user):
        # Allow authentication without a password when creating a superuser
        if user.is_superuser:
            return True
        return super().user_can_authenticate(user)