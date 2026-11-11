# # # *args Function (Variable-Position arguments) accept any number as input and capture the input as a tuple

# def calc_cost(*prices):
#     return sum(prices)

# bill = calc_cost(100, 300, 6500, 450, 12540)
# bill2 = calc_cost(100, 300, 6500, 450, 12540, 1000, 2000)


# print(f"total bills is: {bill}")
# print(f"total bills is: {bill2}")



# # **kwargs Function (Variable-Keyword arguments) capture the input as key-value pairs (dictionary)

# def user_data(**data):
#     for key, value in data.items():
#         print(f"{key.capitalize()} : {value} ")


# user_data(name= "Golu nigam", age = 16, city = "agra")


## Lambda Funcation (Annonymous Funcation) is a function without a name and can take any number of arguments but can only have one expression.

# lambda_fun = lambda a, b,c : a*b+c

# num1, num2, num3 = map(int, input("Enter the values of a,b,c : ").split(","))
# print(f"the result is: {lambda_fun(num1, num2, num3)}")