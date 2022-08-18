password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(" ".join(list(map(lambda word: "".join([(chr(ord(char) + 2)) if char < 'y' and char.isalpha() else
                                              chr(((ord(char)) + 2) - ord('z')) if char.isalpha() else char
                                              for char in word]), password.split()))))
