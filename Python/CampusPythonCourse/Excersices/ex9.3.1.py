def my_mp3_playlist(file_path):
    """
    Function that read mp3 playlist file and create a tuple:
    first value is the song with the longest play time
    second value is the num of songs that playlist is include
    third value is name of singer that have the biggest number of songs in the list.
    :param file_path: The dir of the playlist file
    :return: Tuple with the three values
    :rtype: Tuple
    """
    with open(file_path, 'r') as playlist_file_content:
        file_content_list = playlist_file_content.readlines()
        values_list = [0, len(file_content_list), 0]
        longest_song = [0, ""]
        biggest_count = [0, ""]
        singer_count_list = []
        for i in range(len(file_content_list)):  # For loop that split the each line to list and append singer names
            file_content_list[i] = file_content_list[i].split(";")
            singer_count_list.append(file_content_list[i][0])   # For count purposes

        for i in range(len(file_content_list)):
            file_content_list[i][2] = file_content_list[i][2].split(':')    # Try to find the longest song
            file_content_list[i][2] = int("".join(file_content_list[i][2]))  # make the songs time to a number
            if file_content_list[i][2] > longest_song[0]:
                longest_song[0], longest_song[1] = file_content_list[i][2], file_content_list[i][0]

            # Find the singer with that have the biggest num of songs in the playlist
            if file_content_list[i][0] != singer_count_list[0] and\
                    singer_count_list.count(file_content_list[i][0]) > biggest_count[0]:
                biggest_count[0] = singer_count_list.count(file_content_list[i][0])
                biggest_count[1] = file_content_list[i][1]
        values_list[0] = longest_song[1]    # Longest song
        values_list[2] = biggest_count[1]   # Biggest count singer

        return tuple(values_list)


def main():
    print(my_mp3_playlist(r"d:\songs.txt"))


if __name__ == '__main__':
    main()