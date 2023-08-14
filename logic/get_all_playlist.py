import spotipy

def get_all_playlist(session: spotipy.Spotify):
     
    playlists = session.user_playlists("ladziholmsz", limit=50, offset=0)

    for playlist in playlists["items"]:
        print(playlist["name"])

    return playlists


