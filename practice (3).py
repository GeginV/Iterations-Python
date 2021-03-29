try:
    number_input = int(input(" Type a number "))
except ValueError as e:
    print("You didn't type a number")
else:
    print('You typed ', number_input)
finally:
    print("I'm done")
