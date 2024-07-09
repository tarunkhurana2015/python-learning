def greet(first_name, last_name):
    print(first_name, last_name)


greet("Hello", "Onboard")
######


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Random")
file = open("content.txt", "w")
file.write(message)
######


def increement(number, by=1):
    return number + by


result = increement(2, by=5)  # keyword argument
print(result)


# Default argument
print(increement(10))

# variable arguments
# list [2,3,4,5]
# tuple (2,3,4,5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# variable dictioary using **


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="john")

# scope global

message = "a"


def greet1(name):
    global message
    message = "b"


greet1("hello")
print(message)
