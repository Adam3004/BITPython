def parse_rows(rows):
    # rows = [[int(elem) for elem in row] for row in rows]
    map_row = lambda row: list(map(int, row))
    rows = list(map(map_row, rows))
    return rows

if __name__ == '__main__':
    rows = [
        ["111111", "0", "1", "2", "3", "4", "5"],
        ["222222", "1", "2", "3", "4", "5", "6"],
        ["333333", "5", "4", "3", "2", "1", "0"]
    ]
    print(parse_rows(rows))
