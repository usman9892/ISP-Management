#!/usr/bin/env python
import os
import sys

# ✅ PyInstaller Compatibility Fix
if getattr(sys, 'frozen', False):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'isp_management.settings'

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isp_management.settings')

    # ✅ Django ko initialize karein
    import django
    django.setup()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
