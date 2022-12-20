from collections import Counter
from collections import namedtuple

numbers = [5, 4, 6, 3, 2, 3, 4, 5, 6, 7, 8, 1, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(Counter(numbers))
print(Counter("mississippi"))
sentence = "you will never win if you never begin"
print(Counter(sentence))
print(Counter(sentence.split()))

person = namedtuple("person", ["name","height", "weight"])
michael = person('Michael', 1.76, 79)
print(michael.name)
