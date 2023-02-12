def add_songs(*args):
    songs_dict = dict()
    request = ""
    for song, lyrics in args:
        if song not in songs_dict:
            songs_dict[song] = list()
        songs_dict[song].extend(lyrics)

    for song, lyrics in songs_dict.items():
        request += f"- {song}\n"
        if lyrics:
            request += "\n".join(lyrics) + "\n"

    return request
