import json
data=json.load(open("data.json"))
def translate(word):
	word=word.lower()
	if word in data:
		return data[word]
	else:
		return "word not exist"
	   
word=input("Enter your word")
output=translate(word)
print(output)