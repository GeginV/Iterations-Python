number = 11

if type(number) == int:
    if 100 <= number <= 999:
        if number %2 == 0:
            if number %3 == 0:
                print("Number is good")