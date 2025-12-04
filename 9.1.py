n = int(input("Введите число>>>"))
n_1 = 1

while n_1 <= n:
    if  (n_1 < 5 or n_1 > 9) and (n_1 < 17 or n_1 > 37) and (n_1 < 78 or n_1 > 87 ):
        print(n_1)
    n_1 += 1

