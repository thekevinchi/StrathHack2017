from operator import itemgetter

#paid boolean     - past/last=true, future/next=false
#when/how boolean - 
#howMany int      - amount


possible_keywords = {"thing": ["when", "how"],
                     "time": ["next", "last"],
                     "noun": ["payment", "owe"]
                    }

ACTION_1_NAME = "When is my next payment?"
ACTION_2_NAME = "How much do I owe?"
ACTION_3_NAME = "When was my last payment?"
ACTION_4_NAME = "How much was my last payment?"
ACTION_5_NAME = "How much is my next payment?"

actions_dictionary = {
    ACTION_1_NAME: [False, 1],
    ACTION_2_NAME: [False, 1],
    ACTION_3_NAME: [True, 1],
    ACTION_4_NAME: [True, 1],
    ACTION_5_NAME: [False, 1],
}

#mapping keyword to action dictionary ( like matrices )
#if keyword exists in action, 1 else 0
keyword_to_action_dictionary = {
    "when": {ACTION_1_NAME: 1,
             ACTION_2_NAME: 0,
             ACTION_3_NAME: 1,
             ACTION_4_NAME: 0,
             ACTION_5_NAME: 0},
    "how": {ACTION_1_NAME: 0,
            ACTION_2_NAME: 1,
            ACTION_3_NAME: 0,
            ACTION_4_NAME: 1,
            ACTION_5_NAME: 1},
    "payment" : {ACTION_1_NAME : 1,
              ACTION_2_NAME : 0,
              ACTION_3_NAME: 1,
              ACTION_4_NAME: 1,
              ACTION_5_NAME: 1},
    "owe" : {ACTION_1_NAME : 0,
             ACTION_2_NAME : 1,
             ACTION_3_NAME: 0,
             ACTION_4_NAME: 0,
             ACTION_5_NAME: 0},
    "next": {ACTION_1_NAME : 1,
             ACTION_2_NAME : 0,
             ACTION_3_NAME: 0,
             ACTION_4_NAME: 0,
             ACTION_5_NAME: 1},
    "last": {ACTION_1_NAME : 0,
             ACTION_2_NAME : 0,
             ACTION_3_NAME: 1,
             ACTION_4_NAME: 1,
             ACTION_5_NAME: 0}
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
    action_5_total = 0

    # for the matched keywords in string, find which action the combination tends to go to
    for key in keywords:
        matched_keyword = keywords[key][0]
        action_1_total = action_1_total + keyword_to_action_dictionary[matched_keyword][ACTION_1_NAME]
        action_2_total = action_2_total + keyword_to_action_dictionary[matched_keyword][ACTION_2_NAME]
        action_3_total = action_3_total + keyword_to_action_dictionary[matched_keyword][ACTION_3_NAME]
        action_4_total = action_4_total + keyword_to_action_dictionary[matched_keyword][ACTION_4_NAME]
        action_5_total = action_5_total + keyword_to_action_dictionary[matched_keyword][ACTION_5_NAME]

    action_list = [[ACTION_1_NAME, action_1_total],
                   [ACTION_2_NAME, action_2_total],
                   [ACTION_3_NAME, action_3_total],
                   [ACTION_4_NAME, action_4_total],
                   [ACTION_5_NAME, action_5_total]]

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
