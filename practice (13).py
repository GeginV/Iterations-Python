saved_for_future_calculations = 1
number_of_iterations = 5

for i in range(1, number_of_iterations + 1):
    print("The number saved "
          "from previous step =", saved_for_future_calculations)
    print("The number saved in i =", i)
    saved_for_future_calculations = saved_for_future_calculations * i
    print("UPDATED number"
          " for future calculations =", saved_for_future_calculations)
    print("The end of an ITERATION")
print("The end of CYCLE")
print("The multiplied number is ", saved_for_future_calculations)
