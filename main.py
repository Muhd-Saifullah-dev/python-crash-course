# print("Hello world !!") 
# # print statement 

# # # variable dynamic 
# name='Osama bin ladin'
# age=29

# print(name,age)



# # # input user 
# x=input("Enter name : ")
# print("hello ",x)

# # typecasting


# age=input("Enter your age : ")

# print(type(age))   # type string

# age=input("Enter your age ")
# new_age=int(age)

# print(type(new_age))

# float(),str() ,int() ,bool()


# #  type conversion

# print(1+2.5)
# print(1+int(2.999))



#  sum =>a+b
# a=int(input("enter a : "))
# b=int(input("enter b : "))
# sum=a+b
# print(sum)


# #  string 
# name="Tony Stark"
# print(name.upper())
# print(name.lower())
# print(name)

# print(name.replace("Tony","Iron"))
# print(name)

# print(name.split(" "))
# print(name.find('ark'))

# check for presence
# print("S" in name)  





# Exercise 2 :
# take price of 3 product as input 
# input1=int(input("Enter price of product 1 : "))
# input2=int(input("Enter price of product 2 : "))
# input3=int(input("Enter price of product 3 : "))

# print("Total price of 3 product is : ",input1+input2+input3)
# print("Average price of 3 product is : ",(input1+input2+input3)/3)


# arithmetic operators
# print(1+2)  # addition
# print(1-2)  # subtraction
# print(1*2)  # multiplication
# print(1/2)  # division
# print(5 // 2) # floor division
# print(1%2)  # modulus
# print(1**2) # exponentiation



# assignment operators
# a=5
# a+=5  # a=a+5
# print(a)

# range 

#  range(start,stop,step)
# for i in range(1,10,2):
#     print(i)




# for (i in range(1,11):
#     print(i)


# list 
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print(my_list[0])  # access first element
# print(my_list[-1])  # access last element
# print(my_list[1:4])  # access elements from index 1 to 3
# print(len(my_list))  # length of list
# # print(my_list.append(6))  # add element to the end of list
# print(my_list[-3:-1])  # access last three elements
# print(my_list[::2])  # access every second element
# print(my_list[::-1])  # reverse the list
# print(my_list.count(2))  # count occurrences of an element
# print(my_list.index(3))  # index of an element
# print(my_list.sort())  # sort the list
# print(my_list[-3:])



#  tuple  -> immutable
# my_tuple = (1, 2, 3, 4, 5,4,4)
# print(my_tuple,type(my_tuple))
# print(my_tuple.count(4))  


# set  -> unordered collection of unique elements
# my_set = {1, 2, 3, 4, 5,4,4}
# print(my_set,type(my_set))
# print(my_set.add(6))  # add element to the set
# print(my_set.remove(3))  # remove element from the set
# print(len(my_set),my_set)  # length of set


#  dictionary  -> key value pair
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(my_dict,type(my_dict))
# print(my_dict['name'])  # access value by key


# given a list of roll numbers:[101,105,102,101,108,105,110] print all unique roll numbers in the list 
# given a employee  records in the form of list of tuples where each tuple contain employee id ,empployee name ,salary
#  example [
# (101, 'John', 50000),
# (102, 'Jane', 60000),
# ]
# roll_numbers = [101, 105, 102, 101, 108, 105, 110]
# unique_roll_numbers = set(roll_numbers)
# print(unique_roll_numbers)


# employees = [
#     (101, "John", 50000),
#     (102, "Jane", 60000),
#     (103, "Mike", 55000)
# ]

# user_input = int(input("Enter employee id : "))

# for employee_id, name, salary in employees:
#     if employee_id == user_input:
#         print("ID:", employee_id)
#         print("Name:", name)
#         print("Salary:", salary)




# functions
def greet(name):
    print("Hello", name)

greet("Alice")

def add(a, b):
    return a + b


print(add(5, 3))  # Output: 8

#  module function
import math
print(math.sqrt(16))  # Output: 4.0
print(dir(math))