import re

text = "There is a brown pretty fox"

word_to_find = r"apple"

match = re.search(word_to_find,text)

if match:
    print("word found")

else:
    print("word not founf")

 
