import pickle


def union_sets(group_set1, group_set2):     # function that union sets and return the union set
    return group_set1 | group_set2


def intersection_sets(group_set1, group_set2):  # function that intersection sets and return the intersection set
    return group_set1 & group_set2


def is_subset(group_set1, group_set2):  # function that check in if one set is subset of two sets
    return group_set1 <= group_set2


group_file = open('GroupEveningDetails.dat', 'wb')  # Create binary file
# Create Sets
group_set1 = {"Gitit", "Irit", "Idan"}
group_set2 = {"Ran", "Dan", "Yan", "Ann", "Idan"}
group_file_details_list = []    # Line list to add the to dat file
#   Check the num of meals
number_of_meals = len(group_set1) + len(group_set2)
group_file_details_list.append("The number of meals needed is: " + str(number_of_meals) + '\n')
#   Check the num of gifts (one person gets one although he served in both groups)
group_file_details_list.append("The number of gifts that needed is: " + str(len(union_sets(group_set1, group_set2)))
                               + '\n')  # number of gifts

# check how many people were in both groups
group_file_details_list.append("The people who served in both group are: " +
                               str(len(intersection_sets(group_set1, group_set2))) + '\n')
# Check if one group is subset of two
group_file_details_list.append("Is group one is subset of group two? " + str(is_subset(group_set1, group_set2)) + '\n')
group_set1.discard("Gitit")     # Discard gitit from group one
group_file_details_list.append("Gitit has discarded from group one" + '\n')
# Check if two group is subset of one
group_file_details_list.append("Is group two is subset of group one? " + str(is_subset(group_set2, group_set1)) + '\n')
new_group_set = union_sets(group_set1, group_set2)  # Create union group set
.append("The union list of both group is: " + str(new_group_set) + '\n')
new_group_setgroup_file_details_list.add("Nina")   # add nina to the new group set
group_file_details_list.append("Nina added to new group list" + '\n')
pickle.dump(group_file_details_list, group_file)        # add the list to dat file
group_file.close()
group_file = open('GroupEveningDetails.dat', 'rb')
file_content = pickle.load(group_file)
for line in file_content:   # for loop that print each line
    print(line)
