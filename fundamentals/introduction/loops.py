#   x = 12
#    if x > 50:
#     	print("bigger than 50")
#     else:
#     	print("smaller than 50")
#     # because x is not greater than 50, the second print statement is the only one that will execute

#     x = 55
#     if x > 10:
#     	print("bigger than 10")
#     elif x > 50:
#     	print("bigger than 50")
#     else:
#     	print("smaller than 10")
#     # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

#     if x < 10:
#     	print("smaller than 10")
#     # nothing happens, because the statement is false
    
    for i in range(50):
        print(i)
        
        for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.
