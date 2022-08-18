import math

freq_dict = {"La": 55,
        "Si": 61.74,
        "Do": 65.41,
        "Re": 73.42,
        "Mi": 82.41,
        "Fa": 87.31,
        "Sol": 98
        }


class MusicNotes:
    """
    Iterator class that run on Freq dict and print each freq until it raise stop iteration
    """
    def __init__(self):
        self._pow_count = 0
        self._keys_list = list(freq_dict.keys())
        self._keys_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._keys_index >= len(self._keys_list)-1:
            self._pow_count += 1
            if self._pow_count == 5:
                raise StopIteration()
            else:
                self._keys_index = 1
                return freq_dict[self._keys_list[0]] * (pow(2, self._pow_count))
        else:
            self._keys_index += 1
            return freq_dict[self._keys_list[self._keys_index]] * (pow(2, self._pow_count))


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == '__main__':
    main()