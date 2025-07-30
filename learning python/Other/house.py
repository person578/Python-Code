name = input("What's your name? ")

name = name.title().strip()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slythirin")