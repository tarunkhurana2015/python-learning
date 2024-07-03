# comparasion operator

# conditional statements
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("awesome")
else:
    print("cold")

print("Done")

# ternary operators
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# logical operators
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# shortcut-circut evaluation

# chaining comparassion
age = 18
if 18 <= age < 65:
    print("Eligible")

# For loops
for number in range(3):
    print("message", number, (number + 1) * ".")

for number in range(1, 10, 2):
    print("message", number, (number + 1) * ".")

# For...Else
success = False
for number in range(3):
    print("message.,..")
    if success:
        print("Success")
        break
else:
    print("Error")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")


# Iterables
print(type(5))
print(type(range(5)))
for x in "Python":
    print(x)

# While Loops
number = 100
while number > 0:
    print(number)
    number = number // 2


# Infinite Loops
