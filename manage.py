import os
import sys

# Django settings module set karein (PyInstaller ke liye zaroori hai)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isp_management.settings')

# Django ko initialize karein
import django
django.setup()
