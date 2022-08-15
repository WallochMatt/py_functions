# Example function:
def display_name(name):
    print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


display_name('Mike')
display_name('Ian')
display_name('Nevin')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2


def add_one_to_number(number):
    number_one = 1
    add_one = number + number_one
    return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


result = add_one_to_number(30)

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value

# Problem 1
# Write a function that takes in two numbers
# The logic of the function should add those two numbers together and return a sum
# Capture the returned value in a variable and print it to the console


# Problem 2
# Write a function that takes in two strings
# The logic of the function should concatenate those two strings together and return the concatenated result
# Capture the returned value in a variable and print it to the console


# Problem 3
# Write a function that takes in a string
# The logic of the function should print each character of the string one at a time to the console
# HINT: for loop is one way to do this


# Problem 4
# Write a function that takes in a string
# The logic of the function should print the string to the console but only if that string has three or more characters in it
# If it is less than three characters, then print to the console 'we need a larger string to print!'

# Problem Solved 1
# def add_nums_together(num_1, num_2):
#     sum = num_1 + num_2
#     return sum

# result = add_nums_together(2, 2)
# print(result)

#Problem Solved 2
# def concad_strings(string_1, string_2):
#     fusion = string_1 + string_2
#     return fusion

# mashed_strings = concad_strings("Hello ", "World")
# print(mashed_strings)


# Problem Solved 3
# def lines_up_string(only_string):
#     for char in only_string:
#         print(char)


# in_line = lines_up_string("Smash")
# print(in_line)

# Problem Solved 4
# def checks_for_three(user_string):
#     if len(user_string) >= 3:
#         print(user_string)
#     else:
#         print("we need a larger string to print!")

# checks_for_three(input("Gimme a string: "))