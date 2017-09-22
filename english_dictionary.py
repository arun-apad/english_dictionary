import json
#import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def definition(w):
    if w in data:
        w = w.lower()
        return(data[w])
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s? Enter y for yes and n for no: " % get_close_matches(w,data.keys())[0])
        if yn.lower() == 'y':
            return(data[get_close_matches(w,data.keys())[0]])
        elif yn.lower() == 'n':
            return("That is not a valid english word!")
        else:
            return("Did not recognize the entry :( ")
    else:
        #print(SequenceMatcher(None, "rain", "rainn").ratio())
        #print(get_close_matches(w,data.keys()))
        return("That is not a genuine word!")

word = input("Enter the word: ")
output = definition(word)
if type(output) == list:
    for o in output:
        print(o)
else:
    print(output)
#print("git add")

