
q = input('Введите ваше имя: ')
w = input('Введите вашу фамилию: ')
e = input('Введите год рождения: ')
r = input('Введите город проживания: ')
t = input('Введите ваш Email: ')
y = input('Введите ваш телефон: ')

def anket (q, w, e, r, t, y):
    return ' '.join([q, w, e, r, t, y])
print(anket(w = 'Ivanov', q = 'Leo', e = '1990', r = 'Moscow', t = 'vviiqq@mail.ru', y = '8-999-888-99-88'))