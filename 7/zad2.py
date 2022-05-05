from zad1 import parse_rows


def check_groups(rows):
    tab = [elem[0] for elem in rows if 0 in elem[1:]]
    return len(tab)


if __name__ == '__main__':
    rows = [
        ["111111", "0", "1", "2", "3", "4", "5"],
        ["222222", "1", "2", "3", "4", "5", "6"],
        ["333333", "5", "4", "3", "2", "1", "0"]
    ]
    rows = parse_rows(rows)
    print(check_groups(rows))
