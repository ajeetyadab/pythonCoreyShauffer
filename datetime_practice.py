from datetime import datetime,time

attendance = [
    {
        "name": "Aj",
        "login": "30-06-2026 09:12",
        "logout": "30-06-2026 17:45"
    },
    {
        "name": "Rahul",
        "login": "30-06-2026 08:55",
        "logout": "30-06-2026 18:20"
    },
    {
        "name": "Neha",
        "login": "30-06-2026 09:40",
        "logout": "30-06-2026 16:30"
    }
]



t= time(9,0)
t = datetime.combine(datetime.today(),t)



for employee in attendance:
    login = datetime.strptime(employee["login"],"%d-%m-%Y %H:%M")
    hour = login.hour
    min = login.minute
    

    login_time = time(hour,min)
    login_time = datetime.combine(datetime.today(),login_time)
    
    if t>login_time:
        print(f"{employee["name"]} ontime")

    elif t<login_time:
        print(f"{employee["name"]} late by {login_time-t} mins")

    else:
        print(f"{employee["name"]} ontime")






# for employee in attendance:
#     login = datetime.strptime(employee["login"],"%d-%m-%Y %H:%M")
#     logout = datetime.strptime(employee["logout"],"%d-%m-%Y %H:%M")

#     seconds  = (logout - login).seconds
#     hour = seconds//3600
#     mins = (seconds % 3600)//60

#     print(f"{employee["name"]} \nworked: {hour} hour  {mins} mins ")
    

