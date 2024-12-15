a = [1, 2, 3, 4, 5, 6, 3]
for b in a:
    if b % 2 == 1:
        a.remove(b)
    print(a)