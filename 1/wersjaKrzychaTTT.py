def printLine(l: list):
    print("|" + "|".join(l) + "|")


def printEmptyLine():
    print("-" * 13)


def printTable(l: list):
    for i in range(3):
        printEmptyLine()
        printLine(l[i])
    printEmptyLine()


def checkPlayerWon(l: list):
    for row in l:
        if row[0] == row[1] == row[2] != "   ":
            return True
    for i in range(3):
        if l[0][i] == l[1][i] == l[2][i] != "   ":
            return True
    if l[0][0] == l[1][1] == l[2][2] != "   ":
        return True
    if l[0][2] == l[1][1] == l[2][0] != "   ":
        return True
    return False


field = []

for x in range(3):
    field.append(["   ", "   ", "   "])

end = False
player = False
while not end:
    printTable(field)
    p = "o" if player else "x"
    index = input("Player {}:".format(p))
    # Check if value from user is numeric
    if not index.isnumeric():
        print("Error, the value {} is not numeric!".format(index))
        continue
    index = int(index)
    # Check if position is in range (0,8)
    if index < 0 or index > 8:
        print("Error, index {} is out of scope!".format(index))
        continue
    x = index // 3
    y = index % 3
    # Check if the value on position is empty
    if field[x][y] != "   ":
        print("Error, there is value on position {}".format(index))
        continue
    field[x][y] = " {} ".format(p)

    # Check if player won
    if checkPlayerWon(field):
        print("Player {} has won".format(p))
        printTable(field)
        end = True
    player = not player