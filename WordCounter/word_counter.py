import string

files = {
    "1":"Cities.txt",
    "2":"Fruits.txt",
    "3":"Water.txt",
}

try:
    file_input = input("Hi, Input the name of file: ").strip()
    filename = files.get(file_input)
    if filename:
        filename = filename.lower()
        with open(filename) as f :
            text = f.read()
            for char in string.punctuation:
                text = text.replace(char, "")
            words = text.split()
            frequency = {}
            for word in words:
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
                    


            total_words = len(words)
            unique_words = len(set(words))
            
            print(f"The total words: {total_words}")
            print(f"The unique word set: {unique_words}")
            print(f"word Frequency {frequency}")
    else:
        print("No file")

except FileNotFoundError:
    print("The file you asked can't be found!!!")

            

