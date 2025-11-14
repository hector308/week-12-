# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are part of the collections family in Python
#Creating a list
list1 = [1,2,3,4,5]
print(list1)
print (len(list1))
print(list1[0])
print (list1[1:4])
print(list1[:-1])
#reverse list
print(list1[::-1])
#modify
list1.append(6) #adds 6 to the end of the list
print(list1)
list1.extend([7,8]) #shorcut for adding more than one
print(list1)
list1.pop() #removes the last item
print(list1)
list1.pop(2) #sorts in ascending order
print(list1) 
list1.reverse() #reverses list
print(list1)
list1.reverse()
list1.remove(4) #removes by index
print(list1)
list1.remove(6)
print(list1)
print("!")
#add numbers to 50
list2= list(range(12,120))
list1.append(list2)
print(list1)
list3=list(range(120,620))
list1.append(list3)
print(list1)
print(list1[::3])
#.append() adds one item to the end of the list
#.extend() adds multiple items to the end of the list
#.pop() removes abd returns an item to a given index (default is the last item)
#.remove() removes the fist occurance of a value
#.sort() sorts the list in ascending order
#.reverse() reverses the order of the list
#why is a list more useful than a variable?
#a list can hold multiple values, while a varaible can only hold one
cakes=['chocolate','vanilla','red velvet','carrot']
print(cakes)
#want to change chocolate to strawberry
cakes[0]='strawberry'
print(cakes)
cakes[1]='dark chocolate'
print(cakes)
cakes.pop()
print(cakes)
cakes.insert(2, 'funfetti')
print(cakes)
# Examples:

my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
food=['burger','pizza','tacos','ice cream','cake']
# # Print the second and last item.
print(food[3:])
# # Add a new item using .append().
food.append('burrito')
print(food)
# # Remove the first item using .pop(0).
food.pop(0)
print(food)
# # Reverse your list using .reverse().
food.reverse()
print(food)
# # Create a list of 3 lists (matrix), and access the middle element.


#sets={1,2,3,4,5}
#sets are unorganized collections of unique items
#sets do not support indexing or slicing
#sets are mutable, meaning you can add or remove items
#sets are created using curly brackets {}
#sets do not allow duplicate items
set1={1,2,3,4,5}
print(set1)
print (type(set1))
set1.add(6)
print(set1)
set1.remove(3)
set1(print)
tuple1=(1,2,3,4,5)
print(tuple1)
print(type(tuple1))
print(tuple1[0])
print(tuple1[1:4])
#modyfing tuple leads to error