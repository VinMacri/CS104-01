"""
Vincent Macri
Average Test Score Project
"""
average = 0
total = 0
howManyEntered = 0

howMany = int(input("How many test scores would you like to average? "))

while howManyEntered < howMany:
    testScore = float(input("Enter test score: "))
    total += testScore
    howManyEntered += 1

average = total/howMany
print("The average for the test scores you entered is " + str(round(average, 2)))
