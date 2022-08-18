import random


#  return random number between 0-36
def one_spin_random_number():
    winning_number = random.randint(0, 36)
    return winning_number


# input player and full game with multiply player
def full_game(full_game_list):
    want_to_continue_list = [True] * len(full_game_list)
    player_amount_left = [0] * len(full_game_list)
    for p in range(len(full_game_list)):
        player_amount_left[p] = int(full_game_list[p][-1])
        full_game_list[p][-1] = str(full_game_list[p][-1]) + '\n'

    stop_the_game = False
    round_num = 1
    print("Start the Game :) ...")
    while not stop_the_game:
        print("\n********* Round " + str(round_num) + "*********")
        for p in range(len(full_game_list)):
            if want_to_continue_list[p]:
                current_player_list = full_game_list[p]
                round_text = "********* Round " + str(round_num) + "*********" + '\n'
                current_player_list.append(round_text)
                player_have_enough_money = False
                while not player_have_enough_money:
                    print("\nPlayer ", p + 1, "You have: ", player_amount_left[p], " how much you want to spend?")
                    player_bid_money = number_validation()
                    if player_bid_money > player_amount_left[p]:
                        print("You don't have enough money for this bid\nPlease Try again!")
                    else:
                        player_have_enough_money = True
                player_amount_left[p] = player_amount_left[p] - player_bid_money
                player_bid_money = str(player_bid_money) + '$\n'
                player_bid_text = "Player " + str(p + 1) + " Bids:\n "
                current_player_list.append(player_bid_text)
                current_player_list.append(player_bid_money)
                print("Player ", p + 1, "What which number you want to bet on (0-36)?")
                player_bet_number = bet_number_validation()
                player_bet_number_text = "Player Bet on number:\n"
                current_player_list.append(player_bet_number_text)
                current_player_list.append(player_bet_number)

        print("Ok - everyone bet - Lets see what the Roulette Results will be???\n")
        print("<<< The ball is rolling >>>\n")
        winning_number = one_spin_random_number()
        print("~~~~~~~~~The Winning Number For Round Number: ", round_num, "is Number: ", winning_number, '\n')

        for p in range(len(full_game_list)):
            current_player_list = full_game_list[p]
            if want_to_continue_list[p]:
                player_bet_number = current_player_list[-1]
                player_bet_number = player_bet_number.rstrip('\n')
                if int(player_bet_number) == winning_number:
                    print("Player Number: " + int(p + 1) + "Win!\n")
                    player_earn = current_player_list[-3]
                    player_earn = player_earn.rstrip("$\n")
                    player_earn = int(player_earn) * 2
                    print("Player Earn: " + int(player_earn) + "$\n")
                    player_amount_left[p] = player_amount_left[p] + player_earn
                    winning_number = "The winning Number for Round Number " + str(round_num) + " is " + \
                                     str(winning_number) + " Player Win!" + '\n'
                else:
                    print("Player Number: " + str(p + 1) + " Lose...\n")
                    player_lose = current_player_list[-3]
                    player_lose = player_lose.rstrip("$\n")
                    player_lose = int(player_lose)
                    print("Player Lose: " + str(player_lose) + "$\n")
                    winning_number = "The winning Number for Round Number " + str(round_num) + " is " +\
                                     str(winning_number) + " Player Lose..." + '\n'
                current_player_list.append(winning_number)
                amount_left_text = "Player Have: " + str(player_amount_left[p]) + "$ Money left" + '\n'
                current_player_list.append(amount_left_text)

        for p in range(len(want_to_continue_list)):
            current_player_list = full_game_list[p]
            if player_amount_left[p] == 0:
                print("Player " + str(p+1) + " are out of money\n")
                player_stop_play_text = "Player Num: " + str(p + 1) + "Stop Playing in Round: " + str(round_num) + '\n'
                current_player_list.append(player_stop_play_text)
                want_to_continue_list[p] = False
            else:
                if want_to_continue_list[p]:
                    player_choice = player_choice_validation()
                    if player_choice == 0:
                        want_to_continue_list[p] = False
                        player_stop_play_text = "Player Num: " + str(p+1) + " Stop Playing in Round: " + str(round_num) + '\n'
                        current_player_list.append(player_stop_play_text)

        finish_flag = True

        for p in range(len(want_to_continue_list)):
            if want_to_continue_list[p]:
                finish_flag = False

        if finish_flag:
            stop_the_game = True
            print("Everyone Finish The game On Round " + str(round_num))

        else:
            round_num += 1

    return full_game_list


def number_validation():
    number = -1
    while number <= 0:
        while True:
            try:
                number = int(input())
                break
            except ValueError:
                print("You can enter only integers\nPlease insert number again:")

            if number <= 0:
                print("Please insert Positive number\nPlease insert number again:")

    return number


# bet_number_validation():
def bet_number_validation():
    winning_number = -1
    while winning_number < 0 or winning_number > 36:
        while True:
            try:
                winning_number = int(input())
                break
            except ValueError:
                print("You can enter only integers\nPlease insert number again:")
            finally:
                if winning_number < 0:
                    print("Please insert Positive number\nPlease insert number again:")

                if winning_number > 36:
                    print("You can bet only numbers  0 - 36\nPlease insert the Number Again")

    winning_number = str(winning_number) + '\n'
    return winning_number


def player_choice_validation():
    player_choice = -1
    print("Do want to continue to bet or stop playing?\n")
    while player_choice < 0 or player_choice > 1:
        while True:
            try:
                player_choice = int(input("For Yes please insert 1,For No please insert 0\n"))
                break
            except ValueError:
                print("You can enter only integers")

            if player_choice < 0:
                print("Please insert Positive number")
            if player_choice > 1:
                print("Please enter only the choices number that above")

    return player_choice


print("Welcome to the Roulette\n\n")

print("How much Players will play?")
num_player = number_validation()
full_game_list = []
for i in range(num_player):
    full_game_list.append([0])
for i in range(num_player):
    print("Please insert how much Player Number: " + str(i + 1) + " Want to spend?")
    full_game_list[i][0] = "Player start bid:\n"
    full_game_list[i].append(str(number_validation()))

full_game_list = full_game(full_game_list)
game_result_file = open("RouletteGameResults.txt", 'a')

for i in range(len(full_game_list)):
    current_player_list = full_game_list[i]
    game_result_file.writelines(current_player_list)
game_result_file.close()
