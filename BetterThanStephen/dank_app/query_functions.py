possible_keywords = {"thing": ["when", "how"],
                     "time": ["next", "last"],
                     "noun": ["payment", "owe"]
                    }
#possible_functions = ["when next payment", "how much next payment", ]

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
    thing = keywords["thing"][0]
    time = keywords["time"][0]
    noun = keywords["noun"][0]

    print("thing is: {0}".format(thing))
    print("time is: {0}".format(time))
    print("noun is: {0}".format(noun))

    if thing == "when":
        if time == "next":
            if noun == "payment":
                print(1)
            elif noun == "owe":
                print(2)
        elif time == "last":
            if noun == "payment":
                print(3)
            elif noun == "owe":
                print(4)
    elif thing == "how":
        if time == "next":
            if noun == "payment":
                print(5)
            elif noun == "owe":
                print(6)
        elif time == "last":
            if noun == "payment":
                print(7)
            elif noun == "owe":
                print(8)
        
