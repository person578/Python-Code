loop = int(input("How many times do you want it to loop? "))

if loop == 1:
    print("This will loop 1 times")

elif loop > 0:
    for i in range(loop):
        if i + 1 == loop:
            print("This looped " + str(loop) + " times    " + str(i + 1))
            break
        
        print("This will loop " + str(loop) + " times " + str(i + 1))

else:
    print("It doesn't loop")