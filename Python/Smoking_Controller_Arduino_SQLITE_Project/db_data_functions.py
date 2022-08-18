import sqlite3
import datetime
from typing import Dict


def get_limit_data() -> Dict:
    """
    :return: dict of all limits
    """
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM current_limit_data")
    lim_data = c.fetchone()
    current_limit_data = {"StartHourLimit": lim_data[0],
                          "EndHourLimit": lim_data[1],
                          "AmountOfCigarettesDayLimit": lim_data[2],
                          "AmountOfCigarettesEachHour": lim_data[3]}
    conn.close()
    return current_limit_data


def add_timestamp():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    dt = datetime.datetime.now()
    c.execute("""INSERT INTO smoke_history_data(year,month,day,time) VALUES(?,?,?,?);""", (dt.year, dt.month, dt.day,                                                                 f"{dt.hour}:{dt.minute}"))
    conn.commit()
    conn.close()


# Data array get data functions
def create_today_cigarettes_data_arr():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM smoke_history_data WHERE year=? AND month=? AND day=?",
              (datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))
    cigarettes_data_arr = c.fetchall()
    conn.commit()  # delete later
    conn.close()
    return cigarettes_data_arr


def create_month_cigarettes_data_arr():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM smoke_history_data WHERE year=? AND month=?""",
              (datetime.date.today().year, datetime.date.today().month))
    cigarettes_data_arr = c.fetchall()
    conn.commit()
    conn.close()
    return cigarettes_data_arr


def create_year_cigarettes_data_arr():
    conn = sqlite3.connect('cigarette_box_data.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM smoke_history_data WHERE year=?""", (datetime.date.today().year,))
    cigarettes_data_arr = c.fetchall()
    conn.commit()
    conn.close()
    return cigarettes_data_arr


def create_week_cigarettes_data_arr():
    cigarettes_month_arr = create_month_cigarettes_data_arr()
    cigarettes_week_arr = []
    for one_timestamp in cigarettes_month_arr:
        week_num = datetime.date(one_timestamp[0], one_timestamp[1], one_timestamp[2]).isocalendar()[1]
        if datetime.date.today().isocalendar()[1] == week_num:
            cigarettes_week_arr.append(one_timestamp)

    return cigarettes_week_arr


def create_hour_cigarettes_data_arr():
    cigarettes_day_arr = create_today_cigarettes_data_arr()
    cigarettes_hour_arr = []
    for one_timestamp in cigarettes_day_arr:
        if int(one_timestamp[3].split(':')[0]) == datetime.datetime.now().hour:
            cigarettes_hour_arr.append(one_timestamp)

    return cigarettes_hour_arr


# Information Functions
def how_much_did_you_smoke_today():
    return len(create_today_cigarettes_data_arr())


def how_much_did_you_smoke_this_month():
    return len(create_month_cigarettes_data_arr())


def how_much_did_you_smoke_this_year():
    return len(create_year_cigarettes_data_arr())


def how_much_did_you_smoke_this_week():
    return len(create_week_cigarettes_data_arr())


def how_much_nicotine_you_used():
    print(f"In this week you used {12 * how_much_did_you_smoke_this_week()} ml of nicotine")


def how_much_money_did_you_spend():
    print(f"In this week you spend {1.4 * how_much_did_you_smoke_this_week():.2f} NIS")