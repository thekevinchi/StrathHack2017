import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetterThanStephen.settings')
django.setup()

from django.contrib.auth.models import User

from dank_app.models import UserProfile, Payments

amount_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "1", "2", "3", "4", "5",
               "6", "7", "8", "9", "10"]

possible_keywords = {"question": ["when", "how"],
                     "time": ["next", "last", "due"],
                     "noun": ["payment", "payments", "owe", "loan", "loans"],
                     "amount": amount_list
                     }


def find_keywords(result_string):
    keywords = {"question": [], "time": [], "noun": [], "amount": []}
    split_result = result_string.split(" ")

    for word in split_result:
        word = re.sub(r'\W+', '', word).lower()
        print word
        if word == "all":
            keywords["amount"] = "0"
        elif word in possible_keywords["question"]:
            keywords["question"].append(word)
        elif word in possible_keywords["time"]:
            if word == "due":
                keywords["time"].append("next")
            else:
                keywords["time"].append(word)
        elif word in possible_keywords["noun"]:
            if word == "payments":
                keywords["noun"].append("payment")
            elif word == "loans":
                keywords["noun"].append("loan")
            else:
                keywords["noun"].append(word)
        elif word in possible_keywords["amount"]:
            keywords["amount"].append(word)

    #if no amount is given, default to 1 record
    if len(keywords["amount"]) == 0:
        keywords["amount"].append(1)

    return keywords

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
