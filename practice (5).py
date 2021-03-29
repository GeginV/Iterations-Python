# x = int(input('x'))
# y = int(input('y'))
#
# if x > 0:
#     if y > 0:               # x > 0, y > 0
#          print("Первая четверть")
#     else:                   # x > 0, y < 0
#          print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#          print("Вторая четверть")
#     else:                   # x < 0, y < 0
#          print("Третья четверть")

x = int(input('x'))
y = int(input('y'))

if x and y > 0:
    print('I')
if x < 0 and y > 0:
    print('II')
if y and x < 0:
    print('III')
if x > 0 and y < 0:
    print('IV')
