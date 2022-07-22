with open("dogs_breeds.txt", "a") as a:
    a.write ("hello, this s a new line")
file = open("dogs_breeds.txt","r")
print(file.read())