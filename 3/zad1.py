L = [1, 2, 3, 1, 3, 2, 1, 3, 5, 4, 1, 4, 5, 1, 2, 4, 1, 2, 3, 1, 2]

# 1 sposob
# while 1 in L:
#     L.remove(1)

# 2 sposob
# L = [elem for elem in L if elem != 1]

# 3 sposób
for i in range(len(L)):
    try:
        L.remove(1)
    except ValueError:
        break

print(L)
