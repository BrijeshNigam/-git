def input_Until_User_Stops():
    print("Enter the values of your items (type 'stop' to finish):  ")
    while True:
        user_input = input(" > ")
        if user_input.lower() == "done" or user_input.lower() == "stop":
            break
        yield user_input


    for items in input_Until_User_Stops():
        print(f" Processing {items}")
