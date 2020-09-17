
def make_album(name,title,songs=None):
    if songs:
        musician = f"The {title}'s artist {name.title()} sang {songs} songs "
    else:
        musician = f"The {title}'s artist is: {name.title()}"
    return musician

while True:
    album_name = input("Album Name: ")
    q = input("Do you want to quit (yes/no)? ")
    if q == 'yes':
        break
    album_title = input("Album Title: ")
    total_songs = int(input("Total Songs: "))
    musician = make_album(album_name,album_title,total_songs)
    print(musician)

