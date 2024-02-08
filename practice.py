from collections import Counter

x = [
    "joe",
    "bob",
    "sam",
    "joe",
    "bob",
    "bob",
    "mike",
]
y = {"x": 1, "y": 22, "z": 33, "z": 3, "y": 2}

counter = Counter(y)
print(counter)
