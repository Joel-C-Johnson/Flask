"""
import re

input_string = "I.It's free-to-use, 'no $$$ involved!"

print re.sub(r"\s?([^\w\s'/\-\+$]+)\s?", r" \1 ", input_string)


import string
input = "I love programming with Python-3.3! Do you? It's great... I give it a 10/10. It's free-to-use, no $$$ involved!"
ls = []
    for x in input:
        if x in string.punctuation:
            ls.append(' %s' % x)
        else:
            ls.append(x)

print ''.join(ls)
"""
"""
words = "I love programming with Python-3.3! Do you? It's great... I give it a 10/10. It's free-to-use, no $$$ involved!"
print words.split()
#print ''.join(word)
"""
import re
s = "I.It's fr?ee.g,g-g.g!g(g)g.gt'o-use,no $$$ 'involved'!"
se = re.sub(r"\s?([^\w\s'/+$]+)\s?",r" \1 ",s)
print se
