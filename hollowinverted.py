n = 5

for i in range(n, 0, -1):
    if i == n:
        print("* " * n)
    elif i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")