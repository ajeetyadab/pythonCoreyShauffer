course = ["history","geography","commerce","computer science"]
chapters = ["chapter1","chapter2"]

# ACCESSING AN ELEMENT

print(course[0])
print(course[-1])
# print(course[4])
print(course[0:2])
print(course[2:])

# APPEND
course.append("arts")
print(course)

#INSERT
course.insert(0,"social science")
print(course)

#EXTENDS
course.extend(chapters)

#POP AND REMOVE
course.remove("arts")
print(course)
course.pop()
print(course)


# sort and reverse and sorted 
course.sort()
print(course)
course.sort(reverse=True)
print(course)

course2 = sorted(course)
course3 = sorted(course,reverse=True)
print(course2)
print(course3)


# index
print(course.index("commerce"))
print("history" in course)

# looping a list
print("printing a loop")

for item in course:
    print(item)

for index,item in enumerate(course):
    print(f"{index},{item}")

jointed_text_of_list = "-".join(course)
print(jointed_text_of_list)

# SPLIT

print(jointed_text_of_list.split("-"))