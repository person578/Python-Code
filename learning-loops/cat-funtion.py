def main():
    number = get_number()
    meow()

def get_number():
    while True:
        n = int(input("How many times does the cat meow? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()