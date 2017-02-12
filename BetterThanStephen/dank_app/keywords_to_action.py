import operator

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
    words = query.split()
    result_dict = dict((action, 0) for action in actions)
    for word in words:
        if word in keywords:
            for action_no in keywords[word]:
                action = actions[action_no]
                result_dict[action] += 1
    largest_match = sorted(result_dict.items(), key=operator.itemgetter(1))[-1][1]
    if len([action for action in result_dict if result_dict[action] == largest_match]) > 1:
        return [action for action in result_dict if result_dict[action] == largest_match]
    else:
        return sorted(result_dict.items(), key=operator.itemgetter(1))[-1][0]