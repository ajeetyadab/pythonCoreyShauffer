my_message = "hello world"
multiline_message = """hi this is multiline 
message """

# variable name should be as descriptive as possible

print(my_message)
print(multiline_message)

# checking length 
print(len(multiline_message))

# index
print(multiline_message[0])

#ranges
print(multiline_message[0:5])

#uppercase
print(my_message.upper())

#count
print(my_message.count("l"))

#find
print(my_message.find("l"))
print(my_message.find("universe"))

# replace
new_message = my_message.replace("world","universe")
print(new_message)


# concatinating the string

greeting = "hello"
name = "Aj"
message = greeting + " "+name

print(message)

message = "{}, {} welcome".format(greeting,name)
print(message)

# using f string

message = f"{greeting} {name}"
print(message)