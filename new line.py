with open("dogs_breeds.txt", "a") as file_object:
    file_object.write ("hello, this s a new line")
file = open("dogs_breeds.txt","r")
print(file.read())