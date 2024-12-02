from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_secret = models.CharField(max_length=32, blank=True, null=True)  # OTP secret
    is_mfa_enabled = models.BooleanField(default=False)  # MFA is enabled
    is_mfa_verified = models.BooleanField(default=False)  # First-time MFA verification flag

    def __str__(self):
        return f"{self.user.username}'s Profile"
