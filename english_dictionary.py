import json

data = json.load(open("data.json"))

def definition(w):
    if w in data:
        return(data[w.lower()])
    else:
        return("Is that a word?")

word = input("Enter the word: ")
print(definition(word))