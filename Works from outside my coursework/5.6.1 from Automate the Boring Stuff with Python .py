
def add(dict, lis):
    for i in range(0, len(lis)):
        dict.setdefault(lis[i], 0) #此步创建字典中所需要的键。
    for a in range(0, len(lis)):
        backpack[lis[a]] = backpack[lis[a]] + 1 #此步将列表中的数目依次加到字典的值中。
    return dict

def display(dict):
    print("Your backpack contains:")
    total = 0
    for thing, number in dict.items():
        if number > 1:
            print(str(number) + " " + thing + "s")
            total = total + number
        if number == 1:
            print(str(number) + " " + thing)
            total = total + 1
    print("Total: " + str(total))

backpack = {"potion": 6,
            "coin": 499,
            "dagger": 2,
            "H-bomb": 1,
            "Captain America's shield": 1,
            "Hulk": 30}

dragon_loot = ["potion", "coin", "coin", "Iron Man's suit", "coin", "H-bomb"]

backpack = add(backpack, dragon_loot)
display(backpack)