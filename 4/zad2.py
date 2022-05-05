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


if __name__ == '__main__':
    sciezka = input(">")
    if sciezka == "" or not os.path.isfile(sciezka):
        print("Błędna ściezka")
    else:
        try:
            with open(sciezka, "r") as file:
                tekst = ''
                for i in file.readlines():
                    tekst += i.rstrip()
            print(get_top_k_words(tekst, 1))
            print(get_top_k_words(tekst, 3))
        except Exception as e:
            print(e)
