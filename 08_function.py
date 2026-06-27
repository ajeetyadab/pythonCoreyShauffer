def hello_func():
    print("hello function")

hello_func()


def greeting_func(greetings,name = "you"):
    print(f"{greetings},{name} from greeting_func")

greeting_func("good morning","Aj")



def student_Info(*args,**kwargs):
    print(args)
    print(kwargs)

student_Info("maths","physics","descrete mathMatics",name = "Aj",age = 37)


subjects = ("social science","history")
student_details = {"name":"Ajeet","age":28}

student_Info(*subjects,**student_details)

days_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    return  (year%4 == 0) and (year%100 != 0 or year%400 == 0)


def days_in_month(year,month):
    if not 1<= month <=12:
        return "invalid month"

    if month ==2 and leap_year(year):
        return 29
    else:
        return days_month[month]


print(days_in_month(2001,13))

