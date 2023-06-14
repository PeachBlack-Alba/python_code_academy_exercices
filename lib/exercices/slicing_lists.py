# Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.
#
# Take the list fruits as our example:
#
# fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
# If we want to select the first n elements of a list, we could use the following code:
#
# fruits[:n]
# For our fruits list, suppose we wanted to slice the first three elements.
#
# The following code would start slicing from index 0 and up to index 3. Note that the fruit at index 3 (orange) is not included in the results.
#
# print(fruits[:3])
# Would output:
#
# ['apple', 'cherry', 'pineapple']
# We can do something similar when we want to slice the last n elements in a list:
#
# fruits[-n:]
# For our fruits list, suppose we wanted to slice the last two elements.
#
# This code slices from the element at index -2 up through the last index.
#
# print(fruits[-2:])
# Would output:
#
# ['orange', 'mango']
# Negative indices can also accomplish taking all but n last elements of a list.
#
# fruits[:-n]
# For our fruits example, suppose we wanted to slice all but the last element from the list.
#
# This example starts counting from the 0 index up to the element at index -1.
#
# print(fruits[:-1])
# Would output:
#
# ['apple', 'cherry', 'pineapple', 'orange']

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below:


last_two_elements = suitcase[-2:]

print(last_two_elements)

slice_off_last_three = suitcase[:-3]

print(slice_off_last_three)