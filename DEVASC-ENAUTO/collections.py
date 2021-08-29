from collections import Counter
from collections import defaultdict


"""
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

print(Counter(mylist))

sentence = "How many times does each word show up in this sentence with a word"

print(Counter(sentence.split()))

letters = 'aaaaaabbbbbbccccccdddddddfdd'

c = Counter(letters)

print(c.most_common(1))
"""

# normal dictionary
d = {'a': 10}

print(d['a'])

# default dictionary. Default dictionary allows you to ask for a key that is not present already,
#  it will create that key and assign a default value

dic = defaultdict(lambda: 0)

dic['correct'] = 100

print(dic['correct'])

print(dic['WRONG KEY'])
