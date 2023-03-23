values = ["a", "b", "c", "3", "a", "c", "d", "a", "c"]
new_values = [1, 2, 3, 300, 88, 1000]
list = [4, 1, 4, 2, 3, 3, 4, 4, 4, 4]
# Count a in list
"""
count = values.count("a")

if count > 0:
    n = values.index("a")
    print(n)

    for i in range(count-1):
        n = values.index("a", n + 1)
        print(n)

else:
    print("a not in list")

"""


# check for duplicates
"""
duplicate = []

for item in values:
    if values.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)

print(values)
print(duplicate)
"""

# check > 100
"""
LIMIT = 100
pos = 0
found = False

while pos < len(new_values) and not found:
    if new_values[pos] > LIMIT:
        found = True
    else:
        pos = pos + 1


if found:
    print("Value found at position:", pos)
else:
    print("No elemement > 100")

"""

# Remove all 4`s from list
"""
count = list.count(4)
for i in range(count):
    list.remove(i)

print(list)

"""
while i < len(list):
    if list[i] == 4:
        list.pop(i)
    else:
        i = i + 1
print(list)
