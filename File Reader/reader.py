try:
    user_input = input("Hi, Kindly input file name to access \n 1. Fruits \n 2. Cities \n 3. Water : ")
    if user_input == "1":
        f = open("Fruits.txt")
        print(f.read())
    elif user_input == "2":
        c = open("Cities.txt")
        print(c.read())
    elif user_input == "3":
        w = open("Water.txt")
        print(w.read())
    else:
        print("The file inputed can't be found")
except:
    print("The file you want doesn't exist")
finally:
    if user_input == "1":
        f = open("Fruits.txt")
        f.close()
    elif user_input == "2":
        c = open("Cities.txt")
        c.close()
    elif user_input == "3":
        w = open("Water.txt")
        w.close()
    
