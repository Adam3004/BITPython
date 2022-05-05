import os


def get_top_k_words(tekst: str, k):
    tekst = tekst.replace(',', '')
    tekst = tekst.replace('.', '')
    lista_slow = tekst.split()
    lista_slow = [elem.lower() for elem in lista_slow if elem != '']
    slownik = dict()
    for element in lista_slow:
        slownik[element] = slownik.get(element, 0) + 1
    lista_krotek = list(slownik.items())
    lista_krotek.sort(reverse=True, key=lambda x: x[1])
    return lista_krotek[:k]


def read_text_files(dir_path='./'):
    pliki = os.listdir(dir_path)
    txt = [elem for elem in pliki if elem.split('.')[-1] == 'txt' and os.path.isfile(elem)]
    return txt


if __name__ == '__main__':
    sciezka = input(">")
    try:
        with open(sciezka, "r") as file:
            tekst = ''
            for i in file.readlines():
                tekst += i.rstrip()
        print(get_top_k_words(tekst, 1))
        print(get_top_k_words(tekst, 3))
    except Exception as e:
        print(e)
    Lista = []
    for i in read_text_files():
        with open(i, "r") as file:
            tekst = ''
            for j in file.readlines():
                tekst += j.rstrip()
            Lista.append(tekst)

# import os
#
# def get_top_k_words(tekst: str, k):
#     tekst = tekst.replace(',', '')
#     tekst = tekst.replace('.', '')
#     lista_slow = tekst.split()
#     lista_slow = [elem.lower() for elem in lista_slow if elem != '']
#     slownik = dict()
#     for element in lista_slow:
#         slownik[element] = slownik.get(element, 0) + 1
#     lista_krotek = list(slownik.items())
#     lista_krotek.sort(reverse = True, key = lambda x: x[1])
#     return lista_krotek[:k]
#
#
# def read_text_files(dir_path = "./"):
#     pliki = os.listdir(dir_path)
#     txt = [elem for elem in pliki if elem.split(".")[-1] == "txt" and os.path.isfile(elem)]
#     return txt
#
#
# if __name__ == '__main__':
#     sciezka = input(">")
#
#     try:
#         with open(sciezka, "r") as file:
#             tekst = ''
#             for i in file.readlines():
#                 tekst += i.rstrip()
#         print(get_top_k_words(tekst, 1))
#         print(get_top_k_words(tekst, 3))
#     except Exception as e:
#         print(e)
#     lista = []
#     for i in read_text_files():
#         with open(i, "r") as file:
#             tekst = ''
#             for j in file.readlines():
#                 tekst += j.rstrip()
#             lista.append(tekst)
#
