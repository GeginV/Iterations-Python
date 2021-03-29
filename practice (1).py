year = int(input('Введите год'))
output = (year % 400 == 0) or (( year % 4 == 0) and ( year % 100 != 0))
print(output)