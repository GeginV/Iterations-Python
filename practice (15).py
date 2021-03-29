number = 1
breaker = 1
while number < 1000:
    number **= 2
    breaker += 1
    print('Iteration')
    if breaker > 20:
        print('breaker worked')
        break
print(number)
