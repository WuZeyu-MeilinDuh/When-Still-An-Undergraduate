def display(dict):
    print("Your backpack contains:")
    total = 0
    for thing, number in dict.items():
        print(str(number) + " " + thing)
        total = total + number
    print("Total: " + str(total))

backpack = {"potion": 6,
            "coin": 499,
            "dagger": 2,
            "H-bomb": 1,
            "Captain America's shield": 1,
            "Hulk": 30}

display(backpack)