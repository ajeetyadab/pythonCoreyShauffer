# Comparisons:
# Equal:              ==
# Not Equal:          !=
# Greater Than:       >
# Less Than:          <
# Greater or Equal:   >=
# Less or Equal:      <=
# Object Identity:    is

language = 'Python'

if True:
    print("condition is true")
if False:
    print("condition is false")


if language == "kotlin":
    print("language is python")
else:
    print("no match")


user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("welcome to admin page")
else:
    print("Bad Creds")


a = [1,2,3]
# b = [1,2,3]
b = a

if a == b :
    print("both list are equal")
else:
    print("list are not equal")

# but if we checkl identity using is it will return false

if a is b:
    print("both list have same identity")
else:
    print("both list have different identity")

print(id(a))
print(id(b))

print(id(a)==id(b))