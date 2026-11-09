
# returing a fixed number of values from a function

def get_intput():
    a, b=map(int, input("Enter the values of a,b: ").split())
    return a,b  

values_a, values_b = get_intput()

print(f" a: {values_a}, b: {values_b}")



# Returning a dynamic number of values from a function

def give_input(): 
    print("Enter the multiple values:  ")
    marks = [float(number) for number in input().split()]
    return marks
Sub_makrs = give_input()
print(f"The subjects are: {len(Sub_makrs)}")


# Loop-base multi-line input function


def collect_input(count, item_type= "item "):
    items = []
    for i in range(count):
        item=input(f"Enter the {item_type} {i + 1} ")
        items.append(item)
    return items

# Collect ing 3 items from the user
categories = collect_input(3, "category ")

# Collecting 5 numbers from the user
names = collect_input(2, "Name ")

print("The categories are: ", categories)
print("The names are: ", names)