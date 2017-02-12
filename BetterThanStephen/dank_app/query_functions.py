from query_handling import loan

amount_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "1", "2", "3", "4", "5",
               "6", "7", "8", "9", "10"]

possible_keywords = {"question": ["when", "how"],
                     "time": ["next", "last"],
                     "noun": ["payment", "payments", "owe", "loan", "loans"],
                     "amount": amount_list
                     }


def find_keywords(result_string):
    keywords = {"question": [], "time": [], "noun": [], "amount": []}
    split_result = result_string.split(" ")

    for word in split_result:
        word.lower()
        if word == "all":
            keywords["amount"] = "0"
        elif word in possible_keywords["question"]:
            keywords["question"].append(word)
        elif word in possible_keywords["time"]:
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
    if len(keywords["amount"]) == 0:
        keywords["amount"].append(1)

    print("split_result is: {0}".format(split_result))

    return keywords


def query_db(user_p, keywords):
    if ((len(keywords["question"]) == 0) or (len(keywords["time"]) == 0) or (len(keywords["noun"]) == 0) or (len(keywords["amount"]) == 0)):
        return []

    question = keywords["question"][0]
    time = keywords["time"][0]
    noun = keywords["noun"][0]
    amountKeyword = keywords["amount"][0]

    print("question is: {0}".format(question))
    print("time is: {0}".format(time))
    print("noun is: {0}".format(noun))
    print("amount is: {0}".format(amountKeyword))

    whenBoolean = False
    paidBoolean = False
    amount = 1

    if question == "when":
        whenBoolean = True

    if time == "last":
        paidBoolean = True

    if amountKeyword in amount_list:
        if amountKeyword in {"one", "1"}:
            amount = 1
        elif amountKeyword in {"two", "2"}:
            amount = 2
        elif amountKeyword in {"three", "3"}:
            amount = 3
        elif amountKeyword in {"four", "4"}:
            amount = 4
        elif amountKeyword in {"five", "5"}:
            amount = 5
        elif amountKeyword in {"six", "6"}:
            amount = 6
        elif amountKeyword in {"seven", "7"}:
            amount = 7
        elif amountKeyword in {"eight", "8"}:
            amount = 8
        elif amountKeyword in {"nine", "9"}:
            amount = 9
        elif amountKeyword in {"ten", "10"}:
            amount = 10

    print("real amount is: {0}".format(amount))

    return loan(user_p, paidBoolean, amount)
