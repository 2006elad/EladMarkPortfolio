import sqlite3


def amount_validation():
    num = -1
    is_valid = False
    while not is_valid:
        try:
            num = int(input())
        except ValueError:
            print("You can enter only numbers, please try again! ")
        else:
            if num < 0 or num > 23:
                print("You can enter only amount that bigger than 1, Please insert again! ")
            else:
                is_valid = True
    return num


def hour_input_validation():
    hour = -1
    is_valid = False
    while not is_valid:
        try:
            hour = int(input())
        except ValueError:
            print("You can enter only numbers, please try again! ")
        else:
            if hour < 0 or hour > 23:
                print("You can enter hours only between 0-23, Please insert again! ")
            else:
                is_valid = True
    return hour


def change_restricted_hour_limit():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    print("Please insert the start of the restriction Hour: ")
    start_hour = hour_input_validation()
    print("Please insert the end of the restriction Hour: ")
    end_hour = hour_input_validation()
    c.execute("""UPDATE current_limit_data SET StartHourLimit=?,EndHourLimit=? WHERE ROWID=1""", (start_hour, end_hour))
    conn.commit()
    conn.close()


def change_each_day_amount_of_cigarettes_limit():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    print("Please insert the limit of cigarette each Day: ")
    day_limit = amount_validation()
    c.execute("""UPDATE current_limit_data SET AmountOfCigarettesDayLimit = ? WHERE ROWID=1""", (day_limit,))
    conn.commit()
    conn.close()


def change_each_hour_amount_of_cigarettes_limit():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    print("Please insert the limit of cigarette each Hour: ")
    hour_limit = amount_validation()
    c.execute("""UPDATE current_limit_data SET AmountOfCigarettesEachHour = ? WHERE ROWID=1""", (hour_limit,))
    conn.commit()
    conn.close()