from collections import defaultdict
a = defaultdict(list)
a[(4, 2)].append([0, -1])
if [1, 0] in a[(4, 2)]:
    print("tf")