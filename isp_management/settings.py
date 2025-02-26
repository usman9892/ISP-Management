import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# ✅ PyInstaller Compatibility Fix
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)

SECRET_KEY = 'django-insecure-your-secret-key'

DEBUG = True  # Production me False rakhein
ALLOWED_HOSTS = ['*']  # GitHub Actions aur local environment ke liye

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
