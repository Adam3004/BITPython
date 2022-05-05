import math

with open("colors.txt", 'r') as f:
    colors = [line.strip() for line in f]


def reverse_dict(dictionary: dict):
    newDict = {value: key for key, value in dictionary.items()}

    return newDict


def distance(xa: int, ya: int, za: int, B: str):
    xb, yb, zb = map(int, B.split())

    return math.sqrt((xa - xb) ** 2 * (ya - yb) ** 2 * (za - zb) ** 2)


def find_nearest_point(A: str, reversed_color_dict: dict):
    xa, ya, za = map(int, A.split())
    nearest_distance = 5000000
    nearest_distance_name = ''
    nearest_distance_rgb = ''
    for key, value in reversed_color_dict.items():
        current_distance = distance(xa, ya, za, key)
        if current_distance < nearest_distance:
            nearest_distance = current_distance
            nearest_distance_name = value
            nearest_distance_rgb = key

    return nearest_distance_name, nearest_distance_rgb


def create_dict(colors: list):
    colors_dict = dict()
    for line in colors:
        colour_name, rGB = line.split(":")
        colors_dict[colour_name] = rGB

    return colors_dict


# def colour_checker(r: int, g: int, b: int, color_dict: dict):
#     for key, value in color_dict.items():
#         r_c, g_c, b_c = map(int, value.split())
#         if r_c == r and g_c == g and b_c == b:
#             return 'Color name: ' + key
#
#     return 'Color not found'


def colour_checker_optymalized(rgb: str, reversed_color_dict: dict):
    if rgb in reversed_color_dict:

        return f'Color name: {reversed_color_dict[rgb]}'
    else:
        near_color, near_rgb = find_nearest_point(rgb, reversed_color_dict)

        return f'Color not found, did you mean {near_rgb} {near_color}?'


if __name__ == "__main__":
    color_dict = create_dict(colors)
    # r, g, b = map(int, input().split())
    rgb = input().strip()
    reversed_color_dict = reverse_dict(color_dict)
    # print(colour_checker(r, g, b, color_dict))
    print(colour_checker_optymalized(rgb, reversed_color_dict))
