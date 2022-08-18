word = input("Please enter a word: ")
word = word.replace(" ", "")
word = word.lower()
word_reverse = word[-1::-1]
if word == word_reverse:
    print("OK")
else:
    print("NOT")
