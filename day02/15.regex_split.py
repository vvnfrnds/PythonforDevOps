import re

text = "apple,banana,orange,mangoes"

pattern = r","

new_sentence = re.split(pattern,text)

print("new sentence is:", new_sentence)

print("length",len(text))

print (len(new_sentence))