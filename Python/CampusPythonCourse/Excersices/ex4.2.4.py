import calendar
date = input("Please input date ")
date_list = date.split("/")
day_num = calendar.weekday(int(date_list[2]), int(date_list[1]), int(date_list[0]))
if day_num == 0:
    print("Monday")
elif day_num == 1:
    print("Tuesday")
elif day_num == 2:
    print("Wednesday")
elif day_num == 3:
    print("Thursday")
elif day_num == 4:
    print("Friday")
elif day_num == 5:
    print("Saturday")
elif day_num == 6:
    print("Sunday")
