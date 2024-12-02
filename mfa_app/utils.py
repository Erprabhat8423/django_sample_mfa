import pyotp
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_otp_secret():
    return pyotp.random_base32()

def get_totp_uri(user, secret):
    return pyotp.totp.TOTP(secret).provisioning_uri(
        user.email,
        issuer_name="MyDjangoApp"
    )

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return ContentFile(buffer.read(), name="qrcode.png")
