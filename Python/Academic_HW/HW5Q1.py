BLOCK_PERCENT = 0.035   # Adjust the block percent

def input_and_validation():   # Validate that input in integer
    party_name = input("Please enter the party Name: ")
    votes_file.write("Party Name:\n" + party_name + '\n')
    while True:
        try:
            print("Please  enter the num of votes of ", party_name, " party: ", end='')
            chosen_party_votes_number = int(input())    # Chosen_party is the current party we validate her input
            break
        except ValueError:
            print("You can enter only integers")
    votes_file.write("Number Of Votes:\n" + str(chosen_party_votes_number) + '\n')
    return chosen_party_votes_number


def check_if_party_pass_and_return(passing_num_of_votes, party_name):   # check and reset the party's that doesn't pass
    votes_file.readline()
    num_of_party_votes = int(votes_file.readline())
    if int(num_of_party_votes) < passing_num_of_votes:
        print(party_name, " party doesn't pass the block percent")
        return 0
    return num_of_party_votes


def return_party_name():
    votes_file.readline()
    return votes_file.readline()


def print_final_mandates(num_of_party_votes, moded, party_name):    # print each party and their final mandates
    print(party_name, end='')
    print(" party have ", format((num_of_party_votes / (moded + 1)), '.0f'), "Mandate's")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


votes_file = open('EachPartyVotes.txt', 'w')

#   input each party votes
first_sum_of_votes = 0
for i in range(5):
    first_sum_of_votes = first_sum_of_votes + int(input_and_validation())
votes_file.close()
print('Data written to EachPartyVotes.txt.')

print('\n')
votes_file = open('EachPartyVotes.txt', 'r')
#   Sum of the first votes of all party's (although some of them aren't pass the block percent)
passing_num_of_votes = first_sum_of_votes * BLOCK_PERCENT  # We creating the minimum votes standard (to take out the party's that aren't pass the block percent)

# Check each party if she pass the block percent
apn = return_party_name()
apv = check_if_party_pass_and_return(passing_num_of_votes, apn)
bpn = return_party_name()
bpv = check_if_party_pass_and_return(passing_num_of_votes, bpn)
cpn = return_party_name()
cpv = check_if_party_pass_and_return(passing_num_of_votes, cpn)
dpn = return_party_name()
dpv = check_if_party_pass_and_return(passing_num_of_votes, dpn)
epn = return_party_name()
epv = check_if_party_pass_and_return(passing_num_of_votes, epn)

finalSumOfVotes = apv + bpv + cpv + dpv + epv  # Sum the total votes of the party's that pass the block percent
print(votes_file.read(), '\n')
votes_file.close()

# Calculate each party and her mandate's and then print each party and her final mandate's
moded = finalSumOfVotes / 120   # Create the moded variable (For the mandate's calculation


# print the final mandates of each party

print("\nThe Total Mandate of each party is: ")
print_final_mandates(apv, moded, apn)
print_final_mandates(bpv, moded, bpn)
print_final_mandates(cpv, moded, cpn)
print_final_mandates(dpv, moded, dpn)
print_final_mandates(epv, moded, epn)

