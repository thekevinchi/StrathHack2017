from query_handling import find_keywords, loan, amount_list

def query_db(user_p, query):

    keywords = find_keywords(query)

    if ((len(keywords["question"]) == 0) or (len(keywords["time"]) == 0) or (len(keywords["noun"]) == 0)):
        return []

    question = keywords["question"][0]
    time = keywords["time"][0]
    noun = keywords["noun"][0]
    amount = keywords["amount"][0] if len(keywords["amount"]) > 0 else 1

    whenBoolean = False
    paidBoolean = False

    if question == "when":
        whenBoolean = True

    if time == "last":
        paidBoolean = True

    return loan(user_p, paidBoolean, amount)
