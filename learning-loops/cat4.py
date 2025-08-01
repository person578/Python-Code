while True:
    n = int(input("How many times does the cat meow? "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")