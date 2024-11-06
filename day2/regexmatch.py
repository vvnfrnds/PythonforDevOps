import re

text = "there is a black little fox"  

word = r"there"

match = re.match(word,text) #Used to find only the first word from the sentence

if match:
    print("match found")
else:
    print("match not found")
