import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetterThanStephen.settings')
django.setup()

from django.contrib.auth.models import User

from dank_app.models import UserProfile, Payments


def loan(user, paid, amount):
    if (paid):
        # sort paid payments by (high to low)
        payments = Payments.objects.filter(user=user, paid=True).order_by('-due_date')
    else:
        # sort due payments by (low to high)
        payments = Payments.objects.filter(user=user, paid=False).order_by('due_date')
    if (amount > 0 and amount < len(payments)):
        payments = payments[:amount]

    return payments


# # testing run
# user = User.objects.get(username='bob')
# user_p = UserProfile.objects.get(user_account=user)
#
# payments = loan(user_p, False, 0)
# for payment in payments:
#     print payment
