drawers = ["documents", "envelopes", "pens"]

# access the drawer with index of 0 and print value
print(drawers[0])  # prints documents
# access the drawer with index of 1 and print value
print(drawers[1])  # prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2])  # prints pens

# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers)  # prints ["tchotchkes", "envelopes", "pens"]

# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]

# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers)  # prints ["tchotchkes", "tchotchkes", "pens"]


name = 'Peter'
age = 23

print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')
print(f'{name} is {age}) years old')
