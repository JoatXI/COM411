direction = input("Which direction should beep paint?: ")

if direction == "up":
    print("I am painting in the upward direction")
elif direction == "down":
    print("I am painting in the downward direction")
elif direction == "left":
    print("I am painting towards the left direction")
elif direction == "right":
    print("I am painting towards the right direction")
else:
    print("No direction given")

print("Finished painting!")
