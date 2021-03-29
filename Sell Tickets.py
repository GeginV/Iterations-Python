print('='*5, 'Sell Tickets', '='*5)

total_sum = 0
price_adult, price_young, price_kids = 1390, 990, 0
discount_percent = 10

people = int(input('How many attendants? : '))
people_list = [i for i in range(people)]

for identify_age in people_list:
    age = int(input('What is the age of an attendant? : '))
    if age > 25:
        print("The price for a ticket is : ", price_adult, " rub")
        total_sum += price_adult
    elif 18 <= age <= 25:
        print("The price for a ticket is : ", price_young, " rub")
        total_sum += price_young
    else:
        print("The price for a ticket is : ", price_kids, " rub")
        total_sum += price_kids

if len(people_list) > 3:
    print("Groups of more than 3 get ", discount_percent, "% off!")
    total_sum -= (total_sum // 100 * discount_percent)

print("Your order is : ", total_sum, " rub")
