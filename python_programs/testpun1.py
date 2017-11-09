import string

string ="heloo. how are you$"
for x in string.punctuation:
    if x == "/":
        continue
    if x == "'":
        continue
    if x == "-":
        continue
    if x == "+":
        continue
    if x == "$":
        continue
    input = input.replace(x," %s " % x)
