num_1 = int(input('первое значение'))
num_2 = int(input('второе значение'))
num_3 = int(input('третье значение'))

def my_func(num_1, num_2, num_3):
     if num_1 >= num_2 and num_3 >= num_2:
          return num_1 + num_3
     elif num_2 > num_1 and num_3 > num_1:
          return num_2 + num_3
     else:
          return num_1 + num_2

print(f'Result - {my_func(num_1, num_2, num_3)}')