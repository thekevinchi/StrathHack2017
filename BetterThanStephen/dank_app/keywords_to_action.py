import operator
from query_handling import loan

actions = ['last_payment_time',
           'last_payment_amount',
           'next_payment_time',
           'next_payment_amount',
           'amount_owed'
           ]

keywords = {"when": [0, 2],
            "how": [1, 3, 4],
            "payment": [0, 1, 2, 3],
            "owe": [4],
            "next": [2, 3],
            "last": [0, 1]}

def identify_action(query):
    result_dict = dict((action, 0) for action in actions)
    for word in keywords:
        if word in query:
            for action_no in keywords[word]:
                action = actions[action_no]
                result_dict[action] += 1            
    largest_match = sorted(result_dict.items(), key=operator.itemgetter(1))[-1][1]
    if len([action for action in result_dict if result_dict[action] == largest_match]) > 1:
        return [action for action in result_dict if result_dict[action] == largest_match]
    else:
        return [sorted(result_dict.items(), key=operator.itemgetter(1))[-1][0]]

def query_db(query):
    action = identify_action(query)

    return loan(user_p, paidBoolean, amount)  
