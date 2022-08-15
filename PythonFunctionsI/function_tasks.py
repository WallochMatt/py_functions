




# Task 1: String Manioulation


# def first_n_last(given_string):
#     print(given_string[0] + given_string[-1])

# first_n_last("Packers")


# Task 2: Peanut Buteer and Jelly

#IGNORE
# def pb_j():
#     zero_to_100 = 0
#     while zero_to_100 < 100:    #TRY SIMPLIFYING THIS INTO JUST A FOR LOOP TO USE THE IFS AFTER MORE CLEANLY
#         #zero_to_100 = 0
#         if zero_to_100 < 100:
#             zero_to_100 = zero_to_100 + 1
#             print(zero_to_100)
#         else:
#             break
#IGNORE


# def pb_j():
#     zero_to_100 = 0
#     while zero_to_100 < 100:
#         zero_to_100 = zero_to_100 + 1 
#         #print(zero_to_100)
#         if zero_to_100 % 3 == 0 and zero_to_100 % 5 == 0:
#             print("peanut butter jelly")
#         elif zero_to_100 % 5 == 0:
#             print("jelly")
#         elif zero_to_100 % 3== 0:
#             print("peanut butter")
#         else:
#             print(zero_to_100)

# pb_j()

# Task 3: Word - Letter Indexing

# def indexes_letters(phrase):# loop over user word, 
#     final_result = ""
#     for index in range(len(phrase)):
#         final_result += phrase[index]  + str(index)
#     print(final_result)

# # def lines_up_string(only_string):
# #     for char in only_string:
# #         print(char)

# indexes_letters(input("Type: "))

# Task 4: Ingredient Search

#def food(ingredients):#list in a func?

# def food(ingredients): 
    
#     request = input("What ingredients would you like to search for? ")
#     for index in ingredients: #use a bool, let the loop check then allow user to select
#         while request == index:
#             print(index)
#             return index
#     if request != index:
#         choice = input("We don't have that, would you like to search again?")
#         if choice == "Y":
#             food(ingredients)
#         elif choice == "N":
#             print("Thanks for looking ") 


# ingredient_list = ["apple", "banana", "crust", "blueberry", "cherry"]
# food(ingredient_list)


# Task 5: Reverse a List

# def reversanator(list_of_strings):
#     for x in range(len(list_of_strings)):
#         x = list_of_strings[::-1]
#         return x

# strings_to_try = ["Yellow", "Purple" , "Orange"]
# check = reversanator(strings_to_try)
# print(check)

# Task 6: Drop Four


def checks_leng(names):
    reformed_list = []
    for index in names:
        if len(index) > 4:
            reformed_list.append(index)
    return reformed_list

list_of_names = ["Rebecca", "Sam", "Bob", "Dante", "Monica", "Brad"]
new_list = checks_leng(list_of_names)
print(new_list)