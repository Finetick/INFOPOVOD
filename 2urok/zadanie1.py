 # Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.

a, b =input("Введите числитель и знаменатель через пробел: ").split()

if not a.isdigit() or not b.isdigit():
    print("Введите целые числа!!")
else:
    a, b, = map(int, (a, b))

    if b == 0:
        print(f'Введите знаменатель, отличающийся от нуля')
    else: 
        print(f'Результат деления: ' , a/b)
