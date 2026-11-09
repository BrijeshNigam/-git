# split , comma using input function

from typeguard import value


a,b,c=input("Enter the values of a,b,c: ").split(",")
print(a,b,c)


# multiple values using input function without using comma in spilt.

numbers = [int (a) for a in input("Enter the number as you want: ").split()]
print("The numbers are: ",numbers)


# input using loop 

number = int(input("Enter the number of items you want to enter: "))
items = []

for i in range(number):
    item = input(f"Enter the item: {i + 1} ")
    items.append(item)

print("All entered items are: ", items)
