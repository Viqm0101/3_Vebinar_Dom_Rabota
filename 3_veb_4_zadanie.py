num_1 = int(input('введите чсло: '))
num_2 = int(input('в какую степень возвести? : '))



#Первое решение * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# def stepen (num_1, num_2):
#     perem = num_1 ** num_2
#     return perem
# print(stepen(num_1, num_2))



#второе решение * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def stepen (num_1, num_2):
    res = 1
    for i in range(abs(num_2)):
        res *= num_1
    if num_2 >=0:
        return res
    else:
        return 1 / res
print(stepen(num_1, num_2))