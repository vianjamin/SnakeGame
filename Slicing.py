piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# slicing allows us to access certain elements in list for example if we wanted to print out c,d,e
# this is how we would do it
print(piano_keys[2:5])
# the output is c,d,e this is how the counting works with slicing (we state the position in the list we want to slice
# [0 a 1 b 2 c 3 d 4 e 5 f 6 g 7] so [2:5] the two means we are slicing from c and the 5 means we are stopping before
# f and including e, first number is start and second number is the end, we can also determine how much the increment
# should be
print(piano_keys[2:5:2])
# output is c,e because the last number two means increment of two

# if we want to access the entire array from a certain point lets say we want to print everything from c
print(piano_keys[2:])  # we leave out the second number, and it will automatically print out the rest from position 2

# if we want to print everything up to a certain point we leave out the first number
print(piano_keys[:5])
