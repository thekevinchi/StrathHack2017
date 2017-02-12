import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetterThanStephen.settings')
django.setup()

from django.contrib.auth.models import User

from dank_app.models import UserProfile, Payments


def populate():
    user = add_user(name="Bob",
                    username="bob",
                    password="bob",
                    email="bobby@bobby.com",
                    crn=74747284848,
                    dob="1978-06-23")
    for i in xrange(1, 13):
        add_payment(user=user,
                    payed=True,
                    due_date=datetime(2016, i, 1),
                    amount=600)

    add_payment(user=user,
                payed=True,
                due_date=datetime(2017, 1, 1),
                amount=600)

    add_payment(user=user,
                payed=True,
                due_date=datetime(2017, 2, 1),
                amount=600)

    for i in xrange(3, 13):
        add_payment(user=user,
                    payed=False,
                    due_date=datetime(2017, i, 1),
                    amount=600)

    user = add_user(name="Jen",
                    username="jen",
                    password="jen",
                    email="jen@hotmail.com",
                    crn=93828371023,
                    dob="1982-01-01",
                    status="data entry")

    for i in xrange(1, 13, 3):
        add_payment(user=user,
                    payed=True,
                    due_date=datetime(2016, i, 6),
                    amount=1500)

    add_payment(user=user,
                payed=False,
                due_date=datetime(2017, 3, 2, 10),
                amount=1500)

    add_payment(user=user,
                payed=False,
                due_date=datetime(2017, 5, 8, 10),
                amount=1500)

    user = add_user(name="Jill",
                    username="jill",
                    password="jill",
                    email="jill@media.com",
                    crn=18293255629,
                    dob="1956-09-01")

    for i in xrange(1, 13, 3):
        add_payment(user=user,
                    payed=True,
                    due_date=datetime(2016, i, 6),
                    amount=1200)

    add_payment(user=user,
                payed=False,
                due_date=datetime(2017, 3, 2, 10),
                amount=1700)

    add_payment(user=user,
                payed=False,
                due_date=datetime(2017, 5, 8, 10),
                amount=1500)


def add_user(name, username, password, email, dob,crn, last_name="testuser", status="waiting payment"):
    user = User.objects.create_user(first_name=name, last_name=last_name,
                                    username=username, email=email,
                                    password=password)
    u = UserProfile.objects.get_or_create(user_account=user, dateOfBirth=dob, status=status, crn=crn)[0]
    u.save()
    return u


def add_payment(user, payed=False, due_date=datetime(2017, 12, 31, 10), amount=100):
    payment = Payments.objects.get_or_create(user=user, paid=payed, due_date=due_date, amount=amount)[0]
    payment.save()
    # return payment


if __name__ == '__main__':
    print "Starting the population script..."
    populate()
