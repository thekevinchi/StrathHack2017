from operator import itemgetter

possible_keywords = {"thing": ["when", "how"],
                     "time": ["next", "last"],
                     "noun": ["payment", "owe"]
                    }

#mapping keyword to action dictionary ( like matrices )
#if keyword exist in action, 1 else 0
keyword_to_action_dictionary = {
    "when": {"when is next payment": 1,
             "how much i owe": 0,
             "when is last payment": 1,
             "how much is last payment": 0},
    "how": {"when is next payment": 0,
            "how much i owe": 1,
            "when is last payment": 0,
            "how much is last payment": 1},
    "payment" : {"when is next payment" : 1,
              "how much i owe" : 0,
              "when is last payment": 1,
              "how much is last payment": 1},
    "owe" : {"when is next payment" : 0,
             "how much i owe" : 1,
             "when is last payment": 0,
             "how much is last payment": 0},
    "next": {"when is next payment" : 1,
             "how much i owe" : 0,
             "when is last payment": 0,
             "how much is last payment": 0},
    "last": {"when is next payment" : 0,
             "how much i owe" : 0,
             "when is last payment": 1,
             "how much is last payment": 1}
}

#finding keywords in string
def find_keywords(result_string):
    keywords = {"thing" : [], "time" : [], "noun" : []}
    split_result = result_string.split(" ")

    for word in split_result:
        if word in possible_keywords["thing"]:
            keywords["thing"].append(word)
        elif word in possible_keywords["time"]:
            keywords["time"].append(word)
        elif word in possible_keywords["noun"]:
            keywords["noun"].append(word)

    print("split_result is: {0}".format(split_result))

    return keywords

def query_db(keywords):

    action_1_total = 0
    action_2_total = 0
    action_3_total = 0
    action_4_total = 0

    # for the matched keywords in string, find which action the combination tends to go to
    for key in keywords:
        matched_keyword = keywords[key][0]
        action_1_total = action_1_total + keyword_to_action_dictionary[matched_keyword]["when is next payment"]
        action_2_total = action_2_total + keyword_to_action_dictionary[matched_keyword]["how much i owe"]
        action_3_total = action_3_total + keyword_to_action_dictionary[matched_keyword]["when is last payment"]
        action_4_total = action_4_total + keyword_to_action_dictionary[matched_keyword]["how much is last payment"]

    action_list = [["action 1", action_1_total],
                   ["action 2", action_2_total],
                   ["action 3", action_3_total],
                   ["action 4", action_4_total]]

    # sort and get action with most weight a.k.a chosen action
    sorted_action_list = sorted(action_list, key=itemgetter(1))
    max_action = sorted_action_list[len(sorted_action_list)-1]
    chosen_actions =[[]]
    chosen_actions.append(max_action)

    i=2

    # check if there is more than one action that has same weight
    # if there is, we ask user which one do u want
    while (max_action == sorted_action_list[len(sorted_action_list)-i]):
        chosen_actions.append(sorted_action_list(len(sorted_action_list) - i))
        i = i + 1

    if len(chosen_actions) > 1 :
        for action in chosen_actions:
            print(action)
    elif len(chosen_actions) == 1:
        print(chosen_actions[0][0])
