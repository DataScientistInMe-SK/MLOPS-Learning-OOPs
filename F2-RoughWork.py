# Program to check class of various types of data

my_list = [1,2,3,4]
my_string = " Hawaii"
my_number = 10001

# print("List Type:", type(my_list))
# print("String Type:", type(my_string))
# print("NUmber Type:", type(my_number))

# my_list.clear()
# print("List :", my_list)
# my_list.capitalize()
# print(my_string.capitalize())


## Calling newly created class for OOPS chatbot here
# from Project_OOP import chatbook
# user1 = chatbook()
# print(user1._chatbook__name)

# print("Get:",user1.get_name())
# user1.set_name("Agent")
# print("Set:",user1.get_name())   


## Unique ID creation for different users
from Project_OOP import chatbook

# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)


user1 = chatbook()
print(user1.id)

# Using static method directly from class rtaher than object

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
