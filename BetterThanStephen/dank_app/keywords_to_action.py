import operator

actions = ['last_payment_time',
           'last_payment_amount',
           'next_payment_time',
           'next_payment_amount',
           'amount_owed',
           'display_faq'
           ]

keywords = {"when": [0, 2],
            "how": [1, 3, 4],
            "payment": [0, 1, 2, 3],
            "owe": [4],
            "next": [2, 3],
            "last": [0, 1],
            "due": [2],
            "was": [0, 1],
            "faq": [5],
            "help": [5],
            "assist": [5],
            "frequently": [5],
            "asked": [5],
            "question": [5]}

def identify_action(query):
    # for solving ambiguities
    if query in actions:
        return [query]

    l_query = query.lower()
    result_dict = dict((action, 0) for action in actions)
    for word in keywords:
        if word in l_query:
            for action_no in keywords[word]:
                action = actions[action_no]
                result_dict[action] += 1            
    largest_match = sorted(result_dict.items(), key=operator.itemgetter(1))[-1][1]
    print largest_match
    if len([action for action in result_dict if result_dict[action] == largest_match]) > 1:
        return [action for action in result_dict if result_dict[action] == largest_match]
    else:
        return [sorted(result_dict.items(), key=operator.itemgetter(1))[-1][0]]