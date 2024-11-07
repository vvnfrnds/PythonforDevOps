import re

text = "There is a pretty brown fox"

word_to_find = r"brown"

replacement = "red"

new_sentence = re.sub(word_to_find,replacement,text)

print ("new sentence is:",new_sentence)
