from collections import defaultdict
a = defaultdict(int)
b = a.copy()
b[5] += 1
print(a, b)