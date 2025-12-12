reg = {}
ans = ""
while ans != "3":
    print("""
Please select an option:
1. Register Car
2. Search for a car
3. Exit
""")
    ans = input()

    if ans == "1":

        b = input("Enter the new license plate number:")
        if b in reg:
            print("A car with that license plate is already registered.")
        else:
            reg[b] = {}
            reg[b]["make"] = input("Enter the make of the car:")
            reg[b]["model"] = input("Enter the model of the car:")
            reg[b]["color"] = input("Enter the color of the car:")
            reg[b]["year"] = input("Enter the year of the car(YYYY):")
    elif ans == "2":
        b = input("Enter the license plate number to search:")
        if b in reg:
            print("Year:"+reg[b]["year"])
            print("Make:" + reg[b]["make"])
            print("Model:" + reg[b]["model"])
            print("Color:" + reg[b]["color"])
        else:
            print("No car with that plate found.")

