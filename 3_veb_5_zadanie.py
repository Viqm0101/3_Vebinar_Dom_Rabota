def my_sum():
    n = 0
    d = False
    while d == False:
        num = input('введите значение или 0 для выхода: ').split()
        s = 0
        for i in range(len(num)):
            if num[i] == '0':
                d = True
                break
            else:
                s += int(num[i])
        n += s
        print(f'Значение: {n}')
    print(f'финальная сумма: {n}')
my_sum()