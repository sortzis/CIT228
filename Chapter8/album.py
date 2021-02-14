def make_album(artist, album, songs = "0"):
    artist = {"Artist Name":artist, "Album":album, "Songs":songs}
    for key, value in artist.items():
        print(f"Added = {key}: {value}")

quit = ""

while quit == "":
    band = input("Add Artist: ")
    cd = input("Add Album: ")
    track = input("Add Track Count: ")
    make_album(band, cd, track)
    quit = input("Press 'Q' to quit or enter to add another band!")
    if quit == "q":
        break