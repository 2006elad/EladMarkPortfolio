class UnderAge(Exception):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Your age is {}, the party are only for people that are over 18.\nYou have {} years left, that after" \
               " them you can come to the party".format(self._age, 18-self._age)


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e.__str__())
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation("David", 17)
    send_invitation("Amir", 20)


if __name__ == '__main__':
    main()