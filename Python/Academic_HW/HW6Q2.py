import os


#   Main functions


def menu_validation():  # Function that input and validate menu choice number
    user_choice = -1
    while user_choice < 0 or user_choice > 2:
        while True:
            try:
                print("Please insert 1 for Update vote of the Kneeset member in file")
                print("Insert 2 for Delete Kneeset member Record in file")
                print("Insert 0 if you want to Exit: ")
                user_choice = int(input())
                break
            except ValueError:
                print("You can enter only integers")

            if user_choice < 0:
                print("Please insert Positive number")
            if user_choice > 2:
                print("Please enter only the choices number that above")
    return user_choice


#   Function that update one member vote. The member is found by id. Return the final and updated list
def update_vote(temp_votes_information_list):

    #   input Member ID that we want to update his vote
    print("\nPlease insert the id of the Kneeset member that you want to update his vote: ")
    member_id_we_want_to_found = member_id_validation()
    member_id_we_want_to_found = str(member_id_we_want_to_found) + '\n'

    #   Check if the ID is inside the vote information list. if found update the vote index otherwise print message.
    try:
        index = temp_votes_information_list.index(member_id_we_want_to_found)
        temp_votes_information_list = vote_validation_and_update(temp_votes_information_list, index + 2)
        print("\nWe found this ID in the file")
        print('\nThe vote file has been updated')
    except ValueError:
        print("We didn't found this ID in the file")
        print('\nThe vote file has not been updated')

    return temp_votes_information_list


# Function that delete member by ID we gets from the user. The function delete also multiplies. Return the final list
def delete_mok(temp_votes_information_list):

    #   input Member ID that we want to delete
    print("Please insert the ID of the Kneeset member that you want to update his vote: ")
    member_id_we_want_to_delete = str(member_id_validation())
    index = 4   # First list ID index
    found_member = False

    #   While that loop until we arrive to the end of the list. We find and delete each Record that include the ID
    while index < len(temp_votes_information_list):
        current_member_id = temp_votes_information_list[index]
        current_member_id = current_member_id.rstrip('\n')
        # If we found the member by the ID. we Delete from the record from the list by Record start and end indexes
        if current_member_id == member_id_we_want_to_delete:
            del temp_votes_information_list[index-3:index+4]
            found_member = True
        else:
            index = index + 7

    #   If found any print message
    if found_member:
        print("We found this ID in the file")
        print('\nThe vote file has been updated')
    else:
        print("We didn't found this ID in the file")
        print('\nThe vote file has not been updated')

    return temp_votes_information_list


#   Sub main Function that input and validate user ID we want to search is legal
def member_id_validation():
    member_id = 0
    member_id_digits = -1
    while member_id_digits != 9:
        while True:
            try:
                member_id = int(input("\nPlease Enter Kneeset israel ID (9 digits): "))
                break
            except ValueError:
                print("You can enter only integers")
        member_id_digits = member_id_digit_count(member_id)
        if member_id_digits != 9:
            print("Please Enter again id, israel ID should include 9 digits")

    return member_id


# member_id_validation sub main function that count the id number digits and return the count.
def member_id_digit_count(member_id_digit):
    digit_count = 0
    while member_id_digit != 0:
        member_id_digit = member_id_digit // 10
        digit_count = digit_count + 1
    return digit_count


#   update_vote sub main function that gets the vote list and the index we found that we want to change and update it.
#   the function also gets and validated the new vote choice from the user
def vote_validation_and_update(temp_votes_information_list, index_we_want_to_change):
    member_choice = -1
    while member_choice < 0 or member_choice > 2:
        while True:
            try:
                member_choice = int(input("\nPlease insert 1 for Agree, 2 for Disagree or 0 if you Avoid decision: "))
                break
            except ValueError:
                print("You can enter only integers")

            if member_choice < 0:
                print("Please insert Positive number")
            if member_choice > 2:
                print("Please enter only the choices number that above")

    if member_choice == 1:
        temp_votes_information_list[index_we_want_to_change] = ("Agree" + '\n')
    elif member_choice == 2:
        temp_votes_information_list[index_we_want_to_change] = ("Disagree" + '\n')
    else:
        temp_votes_information_list[index_we_want_to_change] = ("Avoid" + '\n')

    return temp_votes_information_list


#   Main
print("Welcome To the Kneeset of Israel Members vote's delete and update Program\n")
exit_program = False

#   While loop until the user choose to end the program(0 - exit, 1 - to update vote member, 2 - to delete member)
while not exit_program:
    choice = menu_validation()
    if choice != 0:

        #   Read the vote information file and the create temp vote information list
        votes_information = open('VotesInformation.txt', 'r')
        temp_votes_information_list = votes_information.readlines()
        votes_information.close()

        if choice == 1:     # Update member Vote
            temp_votes_information_list = update_vote(temp_votes_information_list)
        else:   # Delete member
            temp_votes_information_list = delete_mok(temp_votes_information_list)

        #   Create temp file, paste the temp list data into the file than overwrite the old vote file with the new one
        temp_information = open('TempVoteInfo.txt', 'w')
        temp_information.writelines(temp_votes_information_list)
        temp_information.close()
        os.remove('VotesInformation.txt')
        os.rename('TempVoteInfo.txt', 'VotesInformation.txt')
        print("\nAll information saved in: VotesInformation.\n\n")

    else:   # Exit Program
        exit_program = True
