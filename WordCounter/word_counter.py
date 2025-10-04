files = {
    "1":"Cities.txt",
    "2":"Fruitd.txt",
    "3": "Water.txt"
}
file_input = input("Hi, Input the name of file: ")
filename = files.get(file_input)
if filename:
    with open(filename) as f:
        print(f.read().lower())
else:
    print("The file inputed can't be found.")



