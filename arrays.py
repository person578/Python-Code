cars = ["Honda", "Chevy", "Mustang", ]
print("We have a Honda, Chevy and a Mustang")
key = int(input("Which car do you want to use? "))

key -= 1

if key < -1:
    print("Enter 1-3")
elif key < -1:
    print(cars[key])