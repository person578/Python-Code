# ask what x and y are
x = float(input("What's x? "))
y = float(input("What's y? "))

# makes variabeles that ask if you want to add subtract etc.
add = input("do you want to add? ")
sub = input("do you want to subtract? ")
mult = input("do you want to multiply? ")
divd = input("do you want to divide? ")

if add == "yes":
    print(f"{x} plus {y} is {x+y}")
elif sub == "yes":
    print(f"{x} minus {y} is {x-y}")
elif mult == "yes":
    print(f"{x} times {y} is {x * y}")
else:
    print(f"{x} divided by {y} is {x / y}")