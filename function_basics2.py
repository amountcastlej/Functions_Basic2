#1. Countdown
# Create a function that accepts a number as an input
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
# create a function that has a placeholder in the parameters
# create a variable to store values of num
# use a for loop to count down from num by 1 until it reaches 0
# every time for loop counts, num gets put into variable 
# return the variable and call the function as a print statement

# def countdown(num):
#     l = []
#     for i in range(num, 0, -1):
#         l.append(i)
#     return l
# print(countdown(5))

#2. Print and Return
# Create a function that will receive a list with two numbers. Print the first value and return the second. 
# create a function with a list placeholder
# print the first number value using an index value of 0
# return the second number value using the index value of 1
# use a print statement beside the function call and have two numbers inside the list

# def print_and_return(num_list):
#     print(num_list[0])
#     return num_list[1]
# print(print_and_return([1,2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# define a function with a placeholder for a list
# return index of the first value in the list
#  add to length of the list and print the sum of the two

# def first_plus_length(list_num):
#     return list_num[0] + len(list_num)
# print(first_plus_length([1, 2, 3, 4, 5]))


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# define a function with a placeholder for a list
# create a variable to hold new list
# Use an if statement to see if values in list are greater than second value
# if values are greater put the value in the new list
# count the number of values greater than the second value
# return the new list and if the list has less than two elements the function returns false

# def greater_than_second(list_num):
#     l = []
#     for num in list_num:
#         if num > list_num[1]:
#             l.append(num)
#     print(len(l))
#     return l
#     if len(list_num) < 2:
#         return False
# print(greater_than_second([5,2,3,2,1,4]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# define a function that accepts two integers

# def length_and_value(size, value):
#     new_list = []
#     for num in range(size):
#         new_list.append(value)
#     return new_list
# print(length_and_value(4,7))

