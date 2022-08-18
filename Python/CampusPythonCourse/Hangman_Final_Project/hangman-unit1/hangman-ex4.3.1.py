guess_letter = input("Guess a letter:")
guess_letter = guess_letter.lower()
if len(guess_letter) > 1 and not guess_letter.isalpha():
    print("E3")
elif len(guess_letter) > 1:
    print("E1")
elif not guess_letter.isalpha():
    print("E2")
else:
    print(guess_letter)
