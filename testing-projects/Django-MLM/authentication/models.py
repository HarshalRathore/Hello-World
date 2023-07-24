import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from twilio.rest import Client
import random


class CustomAccountManager(BaseUserManager):
    def create_user(self, first_name, user_id, phone_number, password, **other_fields):
        if not phone_number:
            raise ValueError(_("You must provide a phone number"))

        if not password:
            raise ValueError(_("You must provide a password"))

        print("Saving user to database")

        user = self.model(
            user_id=user_id,
            first_name=first_name,
            phone_number=phone_number,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, first_name, user_id, phone_number, password, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        super_user = self.model(
            first_name=first_name,
            user_id=user_id,
            phone_number=phone_number,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        super_user.set_password(password)
        super_user.save()
        return super_user


class Profile(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100, blank=True, null=True)

    phone_number = models.CharField(_("phone number"), max_length=20, unique=True)
    email = models.EmailField(_("email address"), max_length=254, blank=True, null=True)

    country = models.CharField(_("country"), max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    phone_number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_timestamp = models.DateTimeField(
        blank=True, null=True
    )  # Timestamp when OTP was generated

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["first_name", "phone_number"]

    def send_otp(self):
        current_time = timezone.now()
        otp = str(random.randint(100000, 999999))

        self.otp = otp
        self.otp_timestamp = current_time

        self.save()

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_NUMBER,
            to=self.phone_number,
        )

        return message.sid

    def verify_otp(self, otp):
        current_time = timezone.now()
        time_difference = datetime.timedelta(minutes=5)

        # Check if OTP was generated within the last 5 minutes
        if self.otp_timestamp and (current_time - self.otp_timestamp) < time_difference:
            if self.otp == otp:
                self.phone_number_verified = True
                self.save()
                return True

        return False

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "User Profiles"
