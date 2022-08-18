import winsound

"""Function that playing Yonatan Hakatan
"""


def main():
    freqs = {
            "la": 220,
            "si": 247,
            "do": 261,
            "re": 293,
            "mi": 329,
            "fa": 349,
            "sol": 392,
            }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    notes_list = notes.split("-")
    notes_list = iter(notes_list)
    while True:
        try:
            next_value = next(notes_list).split(",")
        except StopIteration:
            break
        else:
            winsound.Beep(freqs[next_value[0]], int(next_value[1]))


if __name__ == '__main__':
    main()
