import random

print("What is my magic number (1 to 100) ?")
mynumber = random.randint(1, 100)
ntries   = 1
yourguess= -1
while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + ">> "
    if (ntries == 6) :
        print("your last chance"):
    yourguess = int(input(msg))
    if
        print("--> too high")

        print("--> too low")
        ntries =+1

if
    print("Yes! it's" mynumber)
else :
    print("Sorry! my number is", mynumber)