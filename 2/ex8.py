with open('data.txt', 'r') as f:
    needed = f.readline().strip('\n').split(',')
    _ = f.readline()
    drinks_in_shops = []
    for line in f:
        drinks_in_shop = line.strip('\n').split(',')
        for drink in drinks_in_shop:
            drinks_in_shops.append(drink)


def checker(needed: list, drinks_in_shops: list):
    checked_drinks = {found: False for found in needed}
    not_found_drinks = []
    for drink in drinks_in_shops:
        if drink in checked_drinks:
            checked_drinks[drink] = True
    for key, value in checked_drinks.items():
        if not value:
            not_found_drinks.append(key)
    if len(not_found_drinks) == 0:

        return 'ok'
    else:

        return 'not found: ' + ', '.join(not_found_drinks)


if __name__ == "__main__":
    print(checker(needed, drinks_in_shops))
