BLOCK_PERCENT = 0.035   # Adjust the block percent

# Input by the user each party the votes she gets
A = (int)(input("Please  enter the num of votes of A party "))
B = (int)(input("Please  enter the num of votes of B party "))
C = (int)(input("Please  enter the num of votes of C party "))
D = (int)(input("Please  enter the num of votes of D party "))
E = (int)(input("Please  enter the num of votes of E party "))

firstSumOfVotes = A + B + C +D +E   # Sum of the first votes of all party's (although some of them aren't pass the block percent)
passing_num_of_votes = firstSumOfVotes * BLOCK_PERCENT  # We creating the minimum votes standard (to take out the party's that aren't pass the block percent)

# Check each party if she pass the block percent
if A < passing_num_of_votes:
    A = 0
    print("A party doesn't pass the block percent")
if B < passing_num_of_votes:
    B = 0
    print("B party doesn't pass the block percent")
if C < passing_num_of_votes:
    C = 0
    print("C party doesn't pass the block percent")
if D < passing_num_of_votes:
    D = 0
    print("D party doesn't pass the block percent")
if E < passing_num_of_votes:
    E = 0
    print("E party doesn't pass the block percent")

finalSumOfVotes = A + B + C +D +E # Sum the total votes of the party's that pass the block percent

# Calculate each party and her mandate's and then print each party and her final mandate's
moded = finalSumOfVotes / 120   # Create the moded variable (For the mandate's calculation

mandateOfA = A / moded
mandateOfB = B / moded
mandateOfC = C / moded
mandateOfD = D / moded
mandateOfE = E / moded

print("A party have " , format(mandateOfA,'.0f') , "Mandate's")
print("B party have " , format(mandateOfB,'.0f') , " Mandate's")
print("C party have " , format(mandateOfC,'.0f') , " Mandate's")
print("D party have " , format(mandateOfD,'.0f') , " Mandate's")
print("E party have " , format(mandateOfE,'.0f') ," Mandate's")


