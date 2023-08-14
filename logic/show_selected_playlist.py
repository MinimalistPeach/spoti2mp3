import spotipy

def show_selected_playlist(session: spotipy.Spotify, playlists):
    num = int(input("Adj meg egy playlist indexet: "))
    print("A választott playlist elemei:")
    elements = session.playlist(playlist_id=playlists["items"][num]["id"], fields="tracks(items(track(artists, name)))")

    for element in elements["tracks"]["items"]:
        for artists in element["track"]["artists"]:
            print(artists["name"] + " ", end="")
        print(" - " + element["track"]["name"])