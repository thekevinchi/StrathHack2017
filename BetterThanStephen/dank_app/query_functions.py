# - coding: utf-8 -

from query_handling import find_keywords, loan, status
from keywords_to_action import actions, keywords, identify_action

def query_db(user_p, query):

    action = identify_action(query)
    print action

    if len(action) > 1:
        s = ['Conflict. Did you mean: ']
        for el in action:
            s.append('<a href="?query={0}">{1}</a>'.format(el, el.replace('_', ' ')))
        return s

    keywords = find_keywords(query)

    amount = keywords["amount"][0] if len(keywords["amount"]) > 0 else 1

    if action[0] in {'next_payment_time', 'next_payment_amount'}:
        l = loan(user_p, False, amount)
        l = ['£' + str(x) for x in l]
    elif action[0] in {'last_payment_time', 'last_payment_amount'}:
        l = loan(user_p, True, amount)
        l = ['£' + str(x) for x in l]
    elif action[0] in {'display_faq'}:
        l = ['<a href="/faq">The Frequently Asked Questions can be found here</a>']
    elif action[0] in {'get_status'}:
        l = [status(user_p)]

    
    return l