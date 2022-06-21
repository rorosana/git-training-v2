#Here we are using one simple example to illustrate a function
from random import randrange
# Roll the die three times
for i in range(0, 4):
#Generate random number in the range 1...7
    value = randrange(1, 7)
#Show the die
    print("+-------+")
    if value == 1:
        print("|    |")
        print("| *  |")
        print("|    |")
    elif value == 2:
        print("| *  |")
        print("|    |")
        print("| *  |")
    elif value == 3:
        print("| *  |")
        print("| *  |")
        print("| *  |")
    elif value == 4:
        print("| * * |")
        print("|     |")
        print("| * * |")
    elif value == 5:
        print("| * * |")
        print("| *   |")
        print("| * * |")
    elif value == 6:
        print("| * * * |")
        print("|       |")
        print("| * * * |")
    else:
        print(" *** Error: illegal die value ***")
        print("+-------+")
print(" The Program ran successfully")
#------------------------------------------------------
print("First modification for the 2nd commit")
#------------------------------------------------------
print("Added this line of code from techdevelopers from git terminal")
#------------------------------------------------------
print("Added 1st line from techTeam1 on GitHub")
#------------------------------------------------------
print("Added 2nd line from techTeam1 on GitHub")
