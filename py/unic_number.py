from itertools import permutations

# Define the numbers
numbers = [1, 2, 3, 4]

# Generate all permutations of length 3
perms = permutations(numbers, 3)

# Convert permutations to list and remove duplicates
unique_perms = list(set(perms))

# Print the unique permutations
for perm in unique_perms:
    print(''.join(map(str, perm)))
    



'''
why set without set i will get the same answer?

===Using set is one way
    to remove duplicates from a list of permutations.

why ''join
''.join() is a Python string method used to join 
elements of an iterable into a single string.

'''