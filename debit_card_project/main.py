import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debit_card_project.settings")

import django
django.setup()

from user.models import User

def main():
    User.objects.create(name="Usuario 1",age=12)
    User.objects.create(name="Usuario 2",age=12)

if __name__ == '__main__':
    main()