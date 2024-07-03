course = "Python Programming"
message = """
dc jsdc sdcjds c
sdc jhsdbc

"""
print(len(course))  # length of the string
print(course[5])
print(course[-1])  # end of the string
print(course[0:3])  # first 3 characters of the string
print(course[0:])  # till the end of the string
print(course[:3])
print(course[:])

# Escape sequence
# \"
# \'
# \\
# \n
course1 = "Python \"Programming"
print(course1)

# Formatted String
first = "Tarun"
last = "Khurana"
full = f"{first} {last}"
print(full)

# String Methods
course2 = "  Python Programming   "
print(course2.upper())
print(course2.lower())
print(course2.title())
print(course2.strip())
print(course2.find("Pro"))
print(course2.replace("P", "j"))
print("Pro" in course2)
print("Swift" not in course2)
