import db_data_functions as db_func
import datetime
import time
import os


def this_is_not_restricted_hours():
    limit_data = db_func.get_limit_data()
    curr_hour = datetime.datetime.now().hour
    if limit_data["StartHourLimit"] <= curr_hour < limit_data["EndHourLimit"]:
        print("You can't open - you try to smoke in restricted hours!")
        return False
    return True


def i_did_not_exceed_my_hour_limit():
    limit_data = db_func.get_limit_data()
    if len(db_func.create_hour_cigarettes_data_arr()) < limit_data["AmountOfCigarettesEachHour"]:
        return True
    else:
        print("You can't open - you exceed your amount of cigarettes limit for each hour!")
        return False


def i_did_not_exceed_my_day_limit():
    limit_data = db_func.get_limit_data()
    if len(db_func.create_today_cigarettes_data_arr()) < limit_data["AmountOfCigarettesDayLimit"]:
        return True
    else:
        time.sleep(5)
        print("You can't open - you exceed your amount of cigarettes limit for each day!")
        time.sleep(2)
        return False
