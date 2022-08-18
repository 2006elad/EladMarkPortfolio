class Octopus:
    def __init__(self):
        self.animal_name = "Octavio"
        self.animal_age = 10

    def get_age(self):
        return self.animal_age

    def birthday(self):
        self.animal_age += 1


def main():
    octa_1 = Octopus()
    octa_1.birthday()
    octa_2 = Octopus()
    print("Octa1 age is:", octa_1.get_age())
    print("Octa2 age is:", octa_2.get_age())


if __name__ == '__main__':
    main()