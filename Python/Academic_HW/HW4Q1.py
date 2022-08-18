BLOCK_PERCENT = 0.035   # Adjust the block percent


def input_and_validation(party_name):   # Validate that input in integer
    while True:
        try:
            print("Please  enter the num of votes of ", party_name, " party: ", end='')
            chosen_party = int(input())    # Chosen_party is the current party we validate her input
            break
        except ValueError:
            print("You can enter only integers")
    return chosen_party


def check_if_party_pass_and_update(num_of_party_votes, party_name): # check and reset the partys that doesn't pass
    if num_of_party_votes < passing_num_of_votes:
        num_of_party_votes = 0
        print(party_name, " party doesn't pass the block percent")
    return num_of_party_votes


def print_final_mandates(num_of_party_votes, moded, party_name):    # print each party and their final mandates
    print(party_name, " party have ", format((num_of_party_votes / (moded + 1)), '.0f'), "Mandate's")


#   input each party votes
halikud = input_and_validation("Halikud")
haavuda = input_and_validation("Haavuda")
meretz = input_and_validation("Meretz")
shas = input_and_validation("Shas")
mafdal = input_and_validation("Mafdal")

first_sum_of_votes = halikud + haavuda + meretz + shas + mafdal   # Sum of the first votes of all party's (although some of them aren't pass the block percent)
passing_num_of_votes = first_sum_of_votes * BLOCK_PERCENT  # We creating the minimum votes standard (to take out the party's that aren't pass the block percent)

# Check each party if she pass the block percent
halikud = check_if_party_pass_and_update(halikud, "Halikud")
haavuda = check_if_party_pass_and_update(haavuda, "Haavuda")
meretz = check_if_party_pass_and_update(meretz, "Meretz")
shas = check_if_party_pass_and_update(shas, "Shas")
mafdal = check_if_party_pass_and_update(mafdal, "Mafdal")

finalSumOfVotes = halikud + haavuda + meretz + shas + mafdal # Sum the total votes of the party's that pass the block percent

# Calculate each party and her mandate's and then print each party and her final mandate's
moded = finalSumOfVotes / 120   # Create the moded variable (For the mandate's calculation

# print the final mandates of each party
print("\nThe Total Mandate of each party is: ")
print_final_mandates(halikud, moded, "Halikud")
print_final_mandates(haavuda, moded, "Haavuda")
print_final_mandates(meretz, moded, "Meretz")
print_final_mandates(shas, moded, "Shas")
print_final_mandates(mafdal, moded, "Mafdal")



