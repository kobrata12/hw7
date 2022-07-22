with open("dogs_breeds.txt","r") as reader:
    line = reader.readline()
    while line != '':
        print(line,end = '')
        line = reader.readline()    