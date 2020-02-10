import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    suggestion=get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif len(suggestion)>0:
        YN=input("Did you mean %s instead:If yes press Y else press N"%suggestion[0])
        if YN=='Y' or YN=='y':
            return data[suggestion[0]]
        elif YN=='N' or YN=='n':
            return "Double check the word"
        else:
            return "Invalid input"
    else:
        return "word not exist"
	   
word=input("Enter your word to search")
output=translate(word)
if type(output)==list:
    for i in range(len(output)):
        print(i+1,output[i])
else:
    print("1",output)
#print(output)