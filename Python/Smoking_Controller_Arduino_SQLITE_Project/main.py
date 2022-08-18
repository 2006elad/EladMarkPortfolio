import db_data_functions as db_fun
import limit_settings_config_functions as lim_cg
from arduino import read_box_state
import time


def first_menu_choice():
    choice = -1
    is_valid = False
    while not is_valid:
        try:
            print("""To Open the Box - Press 1
For statistics - Press 2
To change limits - Press 3
To Exit - press 0
Your Answer Here: """)
            choice = int(input())
        except ValueError:
            print("You can enter only integers\n")
        else:
            if 0 <= choice <= 3:
                is_valid = True
            else:
                print("You can enter choices only between 0-3\n")
    return choice


def statistics_menu_choice():
    choice = -1
    is_valid = False
    while not is_valid:
        try:
            print("""How much did you smoke today - press 1
How much did you smoke this week - press 2
How much did you smoke this month - press 3
How much did you smoke this year - press 4
How much money did you spend this week - press 5
How much Nicotine did you use this week - press 6
To Exit to previous menu - press 0
Your Answer Here: """)
            choice = int(input())
        except ValueError:
            print("You can enter only integers\n")
        else:
            if not 0 <= choice <= 5:
                print("You can enter choices only between 0-5\n")
            else:
                is_valid = True
        return choice


def limit_menu_choice():
    choice = -1
    is_valid = False
    while not is_valid:
        try:
            print("""To change the restricted hours - press 1
To change the amount of cigarettes you can smoke each day - press 2
To change the amount of cigarettes you can smoke each hour - press 3
To Exit to previous menu - press 0
Your Answer Here: """)
            choice = int(input())
        except ValueError:
            print("You can enter only integers\n")
        else:
            if not 0 <= choice <= 3:
                print("You can enter choices only between 0-3\n")
            else:
                is_valid = True
        return choice


def main():
    print("~~~~Welcome to Smoke Controller Menu~~~\n")
    is_finish = False
    while not is_finish:
        print("\n~~~Main Menu~~~\n")
        choice_one = first_menu_choice()
        if choice_one == 1:
            read_box_state()

        elif choice_one == 2:
            print("~~~Statistics Menu~~~\n")
            choice_two = statistics_menu_choice()
            if choice_two == 1:     # How much did you smoke today
                print(f"You smoke today {db_fun.how_much_did_you_smoke_today()} cigarettes")
                time.sleep(2)
            elif choice_two == 2:   # How much did you smoke this week - press 2
                print(f"You smoke this week {db_fun.how_much_did_you_smoke_this_week()} cigarettes")
            elif choice_two == 3:   # How much did you smoke this month - press 3
                print(f"You smoke this month {db_fun.how_much_did_you_smoke_this_month()} cigarettes")
            elif choice_two == 4:  # How much did you smoke this month - press 3
                print(f"You smoke this year {db_fun.how_much_did_you_smoke_this_year()} cigarettes")
            elif choice_two == 5:   # How much money did you spend this week - press 4
                db_fun.how_much_money_did_you_spend()
            elif choice_two == 6:   # How much Nicotine did you use this week - press 5
                db_fun.how_much_nicotine_you_used()

        elif choice_one == 3:
            print("~~~Change Limit Settings Menu~~~\n")
            choice_two = limit_menu_choice()
            if choice_two == 1:     # Change the restricted hours - press 1
                print(f"The Restricted Hours now are:\nStart Hours: {db_fun.get_limit_data()['StartHourLimit']}\n"
                      f"End Hour: {db_fun.get_limit_data()['EndHourLimit']}")
                lim_cg.change_restricted_hour_limit()
                print("The Data has been updated successfully!")
            elif choice_two == 2:   # Change the amount of cigarettes you can smoke each day - press 2
                print(f"Your Amount of each day limit is now : {db_fun.get_limit_data()['AmountOfCigarettesDayLimit']}\n")
                lim_cg.change_each_day_amount_of_cigarettes_limit()
                print("The Data has been updated successfully!")
            elif choice_two == 3:   # Change the amount of cigarettes you can smoke each hour - press 3
                print(f"Your Amount of each hour limit is now: {db_fun.get_limit_data()['AmountOfCigarettesEachHour']}\n")
                lim_cg.change_each_hour_amount_of_cigarettes_limit()
                print("The Data has been updated successfully!")
        else:   # Exit
            is_finish = True


if __name__ == '__main__':
    main()
