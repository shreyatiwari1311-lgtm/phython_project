# 1- import the random
import random

# 2- create subjects
subjects = [
    "shahrukh khan",
    "virat kohli",
    "nirmala sitharaman",
    "a mumbai cat",
    "gruop  of work",
    " prime minister of modi",
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "order",
]

places_or_thinds = [
    "at red forts",
    "in mumbai local train",
    "a plote of samosa",
    "inside the gang ghat",
    "during IPL match",
]
# 3- start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thinds = random.choice(places_or_thinds)

    headling = f" BREKING NEWS: {subject} {action} {places_or_thinds}"
    print("\n", headling)

    user_input = input("\nDo you want to another headline? (yes/no)").strip()
    if user_input == "no":
        break
        #p rint goodbye message
        print("\nThanks for using the fake news headline generator. have a fun day")
