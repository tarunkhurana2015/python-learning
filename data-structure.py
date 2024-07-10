from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)

########
print(letters[0:3])
print(letters[:3])
print(letters[0:])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

# unpacking lists
numbers1 = [1, 2, 3, 4, 5, 6]
first, second, third, *other = numbers1
print(other)

# looping over list
for (index, letter) in enumerate(letters):
    print(index, letter)

# add/ remove items from list
letters.append("z")
print(letters)
letters.insert(0, "-")
letters.pop()
print(letters)
letters.remove("b")
print(letters)
del letters[0:3]
print(letters)

# finding object
letters1 = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("s"))

# sorting list
numbers2 = [3, 51, 2, 7, 6]
numbers2.sort()
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# Lamda
items1 = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
items1.sort(key=lambda item: item[1])
print(items1)

# Map fucntion
items2 = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
prices = list(map(lambda item: item[1], items2))
print(prices)

# filter
filtered = list(filter(
    lambda item: item[1] >= 10, items
))
print(filtered)

# list comprehensions [<expression> for item in items]
prices2 = [item[1] for item in items2]
print(prices2)

filtered2 = [item for item in items if item[1] >= 10]
print(filtered2)

# zip
list1 = [1, 2, 3]
list2 = [10, 20, 30]

zipped = list(zip("abc", list1, list2))
print(zipped)

# Stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
browsing_session.pop()
print(browsing_session)

# Queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# tuples  - read only list
point = (1, 2) + (3, 5)
print(type(point))

# swapping variables
x = 10
y = 20
y, x = x, y
print(x, y)

# Arrays

numbers = array("i", [1, 2, 3])
numbers.append(4)

# Sets - unordered Collection with no duplicates
uniques = set([1, 1, 3, 4, 5])
second = {1, 2, 3, 4, 5, 5}
print(second, uniques)
print(second | uniques)

# Dictionaries
point = {"x": 1, "y": 2}
point1 = dict(x=1, y=2)
point["x"]
print(point1.get("a"))
del point1["x"]
for key in point:
    print(key, point[key])
for key, value in point.items():
    print(key, value)

# Dictionary Comprehensions
# [expression for item in items]
values = []
for x in range(5):
    values.append(x * 2)

print(values)
list = [x * 2 for x in range(5)]
print(list)
set = {x * 2 for x in range(5)}
print(set)
dictionary = {x: x * 2 for x in range(5)}
print(dictionary)

# generator expression - generates the numbers in runtime and consume less memory
tuple = (x * 2 for x in range(100005))
print(getsizeof(tuple))

# unpacking Operator
numbers3 = [1, 2, 3]
print(*numbers3)
print(numbers)

#
sentence = "This is a common interview questions"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

tuples = sorted(char_frequency.items(),
                key=lambda kv: kv[1],
                reverse=True)
print(tuples)
