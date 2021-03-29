number = int(input('Введите число '))

while True:
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3 + 1) // 2
    print(number)

    if number == 1:
        print('Done')
        break
