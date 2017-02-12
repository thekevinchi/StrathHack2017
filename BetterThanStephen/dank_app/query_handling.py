import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BetterThanStephen.settings')
django.setup()

from django.contrib.auth.models import User

from dank_app.models import UserProfile, Payments

amount_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
amount_list.extend(str(i) for i in xrange(0, 100))

possible_keywords = {"question": ["when", "how"],
                     "time": ["next", "last", "due"],
                     "noun": ["payment", "payments", "owe", "loan", "loans"],
                     "amount": amount_list
                     }

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

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
            elif word == "owe":
                keywords["noun"].append("payment")
                keywords["time"].append("next")
            else:
                keywords["noun"].append(word)
        elif word in possible_keywords["amount"]:
            print("here")
            if (len(word) > 2):
                keywords["amount"].append(text2int(word))
            else:
                keywords["amount"].append(int(word))

    #if no amount is given, default to 1 record
    if len(keywords["amount"]) == 0:
        keywords["amount"].append(1)

    print keywords

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
