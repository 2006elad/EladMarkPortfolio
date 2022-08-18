file_content = open(r"d:\words.txt", 'r+')
word_file_list = file_content.readlines()
for i in range(len(word_file_list)):
    word_file_list[i] = word_file_list[i].rstrip()

words_string = " ".join(word_file_list)
file_content.close()

file_content = open(r"d:\words.txt", 'w')
file_content.write(words_string)
file_content.close()
