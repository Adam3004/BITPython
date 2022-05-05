def listEnteringAndFormating(namesAndSurnames: list):
    while True:
        data = input('>')
        if data == '':
            break
        temp = data.strip().split()
        temp[0] = temp[0].capitalize()
        temp[1] = temp[1].capitalize()
        namesAndSurnames.append(temp)

    return namesAndSurnames


if __name__ == "__main__":
    namesAndSurnames = []
    print(listEnteringAndFormating(namesAndSurnames))

    with open("names.txt", "w") as file:
        for names in namesAndSurnames:
            file.writelines(' '.join(names))
            file.write('\n')
