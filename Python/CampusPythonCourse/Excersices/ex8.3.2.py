def main():
    """
    Fucntion that make action on a person details dict
    :return: None
    """
    person_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
                   "hobbies": ["Sing", "Compose", "Act"]}
    choice = int(input("Please input number between 1-7: "))
    if choice == 1:
        print("Last name is:", person_dict["last_name"])
    elif choice == 2:
        date_split_list = person_dict["birth_date"].split(".")
        print("The number of month that Mariah born is", date_split_list[1])
    elif choice == 3:
        print("Mariah have", len(person_dict["hobbies"]), "Hobbies")
    elif choice == 4:
        print("Mariah last hobbie is: ", person_dict["hobbies"][-1])
    elif choice == 5:
        person_dict["hobbies"].append("Cooking")
        print(person_dict["hobbies"])
    elif choice == 6:
        date_split_list = person_dict["birth_date"].split(".")
        date_split_tuple = tuple(date_split_list)
        print(date_split_tuple)
    elif choice == 7:
        person_dict["age"] = 20
        print("Mariah age is: ", person_dict["age"])


if __name__ == '__main__':
    main()