from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .utils import generate_otp_secret, get_totp_uri, generate_qr_code
import pyotp
from django.contrib import messages
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@login_required
def enable_mfa(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if not profile.otp_secret:
        profile.otp_secret = generate_otp_secret()
        profile.save()
    otp_uri = get_totp_uri(request.user, profile.otp_secret)
      
    qr_code_file = generate_qr_code(otp_uri)
    
    # Save the QR code temporarily in the default storage
    file_path = default_storage.save("temp_qr_code.png", qr_code_file)
    qr_code_url = default_storage.url(file_path)
    return render(request, 'enable_mfa.html', {'qr_code_url': qr_code_url})

@login_required
def verify_mfa(request):
    if request.method == "POST":
        otp_input = request.POST.get("otp")
        profile = UserProfile.objects.get(user=request.user)
        totp = pyotp.TOTP(profile.otp_secret)
        
        if totp.verify(otp_input):  # OTP is valid
            profile.is_mfa_verified = True  # Mark MFA as verified
            profile.is_mfa_enabled = True  # Enable MFA
            profile.save()

            # Set session variable for MFA verification (optional for this session only)
            request.session["mfa_verified"] = True

            messages.success(request, "MFA setup and verified successfully!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    
    return render(request, "verify_mfa.html")

@login_required
def dashboard(request):
   return render(request, "dashboard.html") 

