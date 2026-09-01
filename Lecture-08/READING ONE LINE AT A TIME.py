with open("example.txt", "r") as file:
    line1 = file.readline()
    while line:
        print(line.strip())
        line1 = file.readline()