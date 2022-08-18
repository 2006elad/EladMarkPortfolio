class Animal:
    """
    A class used to represent an animal
    """
    ZOO_NAME = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def get_hungry(self):
        return self._hunger

    def is_hungry(self):
        """
        Function that return true if the animal is hungry
        :return: True- yes, False- No
        :rtype: bool
        """
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        """
        Function that update that feed the animal by update and reduce the hunger of the animal
        :return: None
        """
        self._hunger -= 1

    def talk(self):
        """
        Method that work on each animal by print the right noise of them
        :return: None
        """
        pass


class Dog(Animal):
    """
    A sub class that used to represent a dog
    """
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        """
        Special dog method
        :return: None
        """
        print("There you go, sir!")


class Cat(Animal):
    """
       Animal sub class that used to represent a cat
    """
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        """
            Special cat method
            :return: None
        """
        print("Meeeeow")


class Skunk(Animal):
    """
       Animal sub class that used to represent a skunk
    """
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        _stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        """
            Special cat method
            :return: None
        """
        print("Dear lord!")


class Unicorn(Animal):
    """
       Animal sub class that used to represent a unicorn
    """
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        """
            Special unicorn method
            :return: None
        """
        print("I’m not your toy...")


class Dragon(Animal):
    """
       Animal sub class that used to represent a dragon
    """
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        """
            Special dragon method
            :return: None
        """
        print("$@#$#@$	")


def check_animals(zoo_lst):
    """
    Sub main function that print the animal that hungry in the list
    :param zoo_lst: list of animals objects
    :type: list
    :return: None
    """
    for animal in zoo_lst:
        if animal.get_hungry() > 0:
            print("{} {}".format(animal.__class__.__name__, animal.get_name()))
            while animal.is_hungry():
                animal.feed()
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            else:
                animal.breath_fire()


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky"), Unicorn("Keith", 7), Dragon("Lizzy", 1450)]
    check_animals(zoo_lst)
    zoo_lst.extend([Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky jr.", 80), Unicorn("Clair", 80),
                    Dragon("McFly", 80)])
    check_animals(zoo_lst)
    print(Animal.ZOO_NAME)


if __name__ == '__main__':
    main()