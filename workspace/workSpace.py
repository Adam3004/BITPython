x = (2, 5, "a", 8, 20,)
print(x.__add__((0,)))
print(x)
lista = [10, 23]
tp = tuple(lista)
print(tp)
l1, l2, c1, l3, l4 = x
print(c1)
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
a, *_, c = lista2
print(a, c)

dict = {"a": 1, "b": 2, (3, 5): 10}
del dict["a"]
print(dict)
print(dict.get("a", 1))
print(dict.get("b", 1))

se = set()
se.add(10)
se.add(20)
print(se)

zbior = set(lista2)
if 2 in zbior:
    print("xd")