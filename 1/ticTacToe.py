import random

pom_list = [i for i in range(1, 10)]
action_list = [' ' for _ in range(9)]


def print_grids(sings_list):
    print(f'''
{sings_list[0]}|{sings_list[1]}|{sings_list[2]}
-+-+-
{sings_list[3]}|{sings_list[4]}|{sings_list[5]}
-+-+-
{sings_list[6]}|{sings_list[7]}|{sings_list[8]}
''')


def sprawdzarka(l1):
    for i in range(3):
        if l1[i] == l1[i + 3] == l1[i + 6]:
            return l1[i]
        if l1[0 + 3 * i] == l1[1 + 3 * i] == l1[2 + 3 * i]:
            return l1[0 + 3 * i]
    if l1[0] == l1[4] == l1[8]:

        return l1[4]
    elif l1[2] == l1[4] == l1[6]:

        return l1[4]

    return '_'


def checker(index, list):
    if type(index) != int:
        print("Bad type of input, you have to enter a number")

        return False
    elif index < 1 or index > 9:
        print("You can choose field from 1 to 9 only")

        return False
    elif list[index - 1] != ' ':
        print("This field is not empty")

        return False

    return True


signs = ['x', 'o']
i = random.randint(0, 1)
reapiting = 0
print_grids(pom_list)
while True:
    if i == 0:
        index = int(input('Enter number of field in which u want to put x: '))
        if not checker(index, action_list):
            continue
        action_list[index - 1] = 'x'
    else:
        index = int(input('Enter number of field in which u want to put y: '))
        if not checker(index, action_list):
            continue
        action_list[index - 1] = 'o'
    if i == 0:
        i = 1
    else:
        i = 0

    sign = sprawdzarka(action_list)
    if signs.__contains__(sign):
        print(f'{sign} won')
        print_grids(action_list)

        break
    elif reapiting == 9:
        print("draw")
        print_grids(action_list)

        break
    reapiting += 1
    print_grids(action_list)

