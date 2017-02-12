from query_handling import find_keywords, loan, amount_list

def query_db(user_p, query):

    keywords = find_keywords(query)

    if ((len(keywords["question"]) == 0) or (len(keywords["time"]) == 0) or (len(keywords["noun"]) == 0) or (len(keywords["amount"]) == 0)):
        return []

    question = keywords["question"][0]
    time = keywords["time"][0]
    noun = keywords["noun"][0]
    amountKeyword = keywords["amount"][0]

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

    return loan(user_p, paidBoolean, amount)
