from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class MFARequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            profile = getattr(request.user, "userprofile", None)
            if profile and profile.is_mfa_enabled:
                if not request.session.get("mfa_verified", False):
                    return redirect("verify_mfa")
