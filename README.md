# Django Sample MFA

A sample Django project demonstrating the implementation of Multi-Factor Authentication (MFA) using OTP-based Google Authenticator.

---

## Features
- User registration and login system.
- Multi-Factor Authentication (MFA) using OTP (One-Time Password).
- Google Authenticator integration for OTP generation and verification.
- QR code generation for easy OTP setup.
- Token-based authentication for secure API access.

---

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default, can be configured)
- **Authentication**: JWT and Google Authenticator
- **Dependencies**:
  - `pyotp` - OTP generation and verification
  - `qrcode` - QR code generation
  - `Pillow` - Image processing

---

## Setup Instructions

### Prerequisites
- Python (>=3.8)
- pip (Python package manager)
- Git

---

### 1. Clone the Repository
```bash
git clone https://github.com/Erprabhat8423/django_sample_mfa.git
cd django_sample_mfa
