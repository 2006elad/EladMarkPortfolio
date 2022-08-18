class BigThing:
    def __init__(self, some_object):
        self._some_object = some_object

    def size(self):
        if isinstance(self._some_object, int):
            return self._some_object
        elif isinstance(self._some_object, dict) or isinstance(self._some_object, list) \
                or isinstance(self._some_object, str):
            return len(self._some_object)
        else:
            return None


class BigCat(BigThing):
    def __init__(self, some_object, weight):
        BigThing.__init__(self, some_object)
        self._weight = weight

    def size(self):
        super().size()
        if 15 < self._weight <= 20:
            print("Fat")
        elif self._weight > 20:
            print("Very Fat")


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    cutie.size()


if __name__ == '__main__':
    main()

