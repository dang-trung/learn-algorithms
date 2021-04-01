import sys
data = []
n = 15

for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"Length: {a}; Size in bytes: {b}.")
    data.append(None)