A = int(input('Digit A '))
B = int(input('Digit B '))
C = int(input('Digit C '))
D = 45
if ((A < D) and (B >= D) and (C >= D)) or\
        ((A >= D) and (B < D) and (C >= D)) or\
        ((A >= D) and (B >= D) and (C < D)):
    print('Condition')
else:
    print('No condition')
