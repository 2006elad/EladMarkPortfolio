# main functions

# function that input one member data(name,id,choice) from the user. The data is inserted to the main list
def vote(vote_information_list, vote_record_num):
    # Member Name Input
    votes_information_list.append("Member Name:\n")
    member_name = member_name_validation()
    votes_information_list.append(member_name + '\n')

    # Member ID Input
    member_id = member_id_validation(votes_information_list)
    votes_information_list.append("Member ID:" + '\n')
    votes_information_list.append(str(member_id) + '\n')

    # Member vote Choice Input
    votes_information_list.append("Member vote choice:" + '\n')
    member_choice = member_choice_validation()
    if member_choice == 1:
        votes_information_list.append("Agree" + '\n')
    elif member_choice == 2:
        votes_information_list.append("Disagree" + '\n')
    else:
        votes_information_list.append("Avoid" + '\n')

    # each record ending line with numbering
    votes_information_list.append("********* " + "End of vote Record Number " + str(vote_record_num)
                                  + " **********" + '\n')

    return vote_information_list


# function that count each vote to one list (each index different choice) than print the final result
def all_votes_info(updated_votes_information_list):
    votes_count_results = [0, 0, 0]  # index 0 - Avoid, 1 - Agree, 2 - Disagree
    index = 6  # The first vote list index

    # While loop that run and count each vote
    while index < len(updated_votes_information_list):
        mok_choice = what_did_he_voted(updated_votes_information_list[index])  # mok choice gets the choice index
        votes_count_results[mok_choice] = votes_count_results[mok_choice] + 1  # count the choice by mok choice
        index = index + 7  # The next vote list index

    #   We print the final result
    if votes_count_results[1] > votes_count_results[2]:
        print("We have coalition!\nWe have: " + str(votes_count_results[1]) +
              " Agree and " + str(votes_count_results[2]) + " Disagree")
    else:
        print("We Don't have coalition!\nWe have: " + str(votes_count_results[2]) +
              " Disagree and " + str(votes_count_results[1]) + " Agree")


# Menu function that want to know if the user is want to add more kneeset members or finish the vote input
def continue_to_vote():
    continue_to_vote_choice = -1
    while continue_to_vote_choice < 0 or continue_to_vote_choice > 1:
        while True:
            try:
                print("\nDo want to add Kneeset members? If yes - Press 1. If not Press 0: ")
                continue_to_vote_choice = int(input())
                break
            except ValueError:
                print("You can enter only integers")

            if continue_to_vote_choice < 0:
                print("Please insert Positive number")

            if continue_to_vote_choice > 1:
                print("Please enter only the choices number that above")

    if continue_to_vote_choice == 1:
        return False
    else:
        return True


#  Vote function sub_functions

# function that gets from the user the name of the member and validated that it is with letter only. return the name
def member_name_validation():
    does_name_include_only_letter = False
    while not does_name_include_only_letter:
        first_name = input("\nPlease insert the first name of the Kneeset member: ")
        last_name = input("Please insert the last name of the Kneeset member: ")
        if first_name !="" and last_name != "":
            #   If first or last name is false - that we loop again and input again from the user
            does_name_include_only_letter = first_name.isalpha() and last_name.isalpha()
            if not does_name_include_only_letter:
                 print("\nPlease enter first and the last names with letters only!\n")
        else:
            print("\nLast name or First Name are empty, Please insert again both of them!")
    full_member_name = first_name + " " + last_name
    return full_member_name


# function that gets from the user the id of the member and validated it legal id input. return the ID
def member_id_validation(votes_information_list):
    member_id = 0
    member_id_digits = -1
    is_member_id_found = True

    # While that loop until we have 9 digits id and validated that the id number isn't appear before
    while member_id_digits != 9 or is_member_id_found:
        while True:
            try:
                member_id = int(input("\nPlease Enter Kneeset israel ID (9 digits): "))
                break
            except ValueError:
                print("You can enter only integers")
        member_id_digits = member_id_digit_count(member_id)
        if member_id_digits != 9:
            print("Please Enter again id, israel ID should include 9 digits")

        else:
            is_member_id_found = member_id_is_not_used(member_id, votes_information_list)
            if is_member_id_found:
                print("The id is already used for another Kneeset Member, Please insert the ID again")

    return member_id


def member_choice_validation():  # Function that gets member choice and validated. return the choice number
    member_choice = -1
    while member_choice < 0 or member_choice > 2:
        while True:
            try:
                member_choice = int(input("\nPlease insert 1 for agree, 2 for disagree or 0 if you avoid decision: "))
                break
            except ValueError:
                print("You can enter only integers")
            finally:
                if member_choice < 0:
                    print("Please insert Positive number")
                if member_choice > 2:
                    print("Please enter only the choices number that above")

    return member_choice


# member_id_validation sub main functions

# member_id_validation sub main function that count the id number digits and return the count.
def member_id_digit_count(member_id_digit):
    digit_count = 0
    while member_id_digit != 0:
        member_id_digit = member_id_digit // 10
        digit_count = digit_count + 1
    return digit_count


# Function that make sure the id number didn't appear before in the list return true if id founded
def member_id_is_not_used(member_id, votes_information_list):
    member_id = str(member_id) + '\n'
    if member_id in votes_information_list:
        return True
    else:
        return False


#   all_votes_info sub main functions
def what_did_he_voted(mok_vote):  # Function that get vote string, strip it and return choice number
    mok_vote = mok_vote.strip('\n')
    if mok_vote == "Agree":
        return 1
    elif mok_vote == "Disagree":
        return 2
    else:
        return 0


# Main
print("Welcome To the Kneeset of Israel Members Voting Program\n")
votes_information_list = ["Members of Knesset Votes Information:\n"]    # Creating vote list information
count_of_voters = 0   # Count the num of voters
end_of_votes = continue_to_vote()

# loop and input member information and vote until the user finish to insert
while not end_of_votes:
    sum_of_voters = count_of_voters + 1
    votes_information_list = vote(votes_information_list, count_of_voters)
    end_of_votes = continue_to_vote()
    print("")

#   Print num of members that voted
print("The total of Kneeset member that were voted is: " + str(count_of_voters))

#   File vote create by the list
votes_information = open('VotesInformation.txt', 'w')
votes_information.writelines(votes_information_list)
votes_information.close()
print("\nAll information saved in: VotesInformation.txt")

#   Create list from vote information File
updated_votes_information = open('VotesInformation.txt', 'r')
updated_votes_information_list = updated_votes_information.readlines()
updated_votes_information.close()

#   Check and print the final result
all_votes_info(updated_votes_information_list)
