class Octopus:
    count_animal = 0

    def __init__(self, name="Octavio"):
        self._animal_name = name
        self._animal_age = 10
        Octopus.count_animal += 1

    def set_name(self):
        print("What is the new name of the animal you want?")
        name = input()
        self._animal_name = name

    def get_name(self):
        return self._animal_name


def main():
    print("What is the name of first animal?")
    name = input()
    octa_1 = Octopus(name)
    octa_2 = Octopus()
    print("Octa1 name is:", octa_1.get_name())
    print("Octa2 name is:", octa_2.get_name())
    octa_2.set_name()
    print(octa_2.get_name())
    print("Num of animals is:", Octopus.count_animal)


if __name__ == '__main__':
    main()
