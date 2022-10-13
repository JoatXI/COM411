print("Program started!")

user_input = input()

len(input("Please enter a standard character: "))

if len(user_input) == 1:
    print(f"The ASCII code for {user_input} is: {ord(user_input)}")
else:
    print("invalid user input")

print("Program Ended!")
