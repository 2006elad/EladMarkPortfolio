def my_mp4_playlist(file_path, new_song):
    """
    Function that change the name of the third line song and print the whole playlist
    :param file_path: dir of playlist file
    :type file_path: str
    :param new_song: The name of the new songs
    :type new_song:str
    :return: None
    """
    playlist_file = open(file_path, 'r+')
    playlist_content_list = playlist_file.readlines()
    if len(playlist_content_list) < 3:
        playlist_content_list.insert(0, '\n')
        playlist_content_list.insert(0, '\n')
    playlist_content_list[2] = playlist_content_list[2].split(";")
    playlist_content_list[2][0] = new_song
    playlist_content_list[2] = ";".join(playlist_content_list[2])
    playlist_file.seek(0)
    playlist_file.truncate(0)
    playlist_file.writelines(playlist_content_list)
    playlist_file.seek(0)
    print(playlist_file.read())


def main():
    my_mp4_playlist(r"d:\songs.txt", "Python Love Story")


if __name__ == '__main__':
    main()
