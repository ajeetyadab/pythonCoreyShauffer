nums = [1,2,3,4,5]

for item in nums:
    if item == 3:
        continue
    elif item ==5:
        break
    else:
        print("value is not equal to three")


for i in range(10):
    print(i)

for i in range(1,10): # last value is not included
    print(i)


# WHILE LOOP

x = 0
while x <10:
    print(f" x is {x}")
    x +=1
