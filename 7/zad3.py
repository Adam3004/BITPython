def refactor(list_of_data: list):
    list_of_data = [elem.strip().capitalize().replace(' ', '') for elem in list_of_data]
    return list_of_data


def get_salaries(names: list, surnames: list, db_data: dict):
    names = refactor(names)
    surnames = refactor(surnames)
    return {tup_name: db_data[tup_name] for tup_name in zip(names, surnames) if tup_name in db_data}


if __name__ == '__main__':
    names = ["JAn", "Aleksandr a", "MariaN "]
    surnames = ["kowalski", "NonaMe", "Nikt"]
    db_data = {
        ("Jan", "Kowalski"): 5000,
        ("Aleksandra", "Noname"): 4000,
        ("Marian", "Nikt"): 3000,
        ("Janina", "Ktoś"): 10000,
        ("Wojciech", "Szef"): 20000
    }
    print(get_salaries(names, surnames, db_data))
