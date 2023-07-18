import spotipy
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials
import json

env = dotenv_values("./config/.env")

CLIENT_ID = env["CLIENT_ID"]
CLIENT_SECRET = env["CLIENT_SECRET"]

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)

session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = session.user_playlists("ladziholmsz", limit=50, offset=0)

for playlist in playlists["items"]:
    print(playlist["name"])


num = int(input("Adj meg egy playlist indexet: "))
print("A választott playlist elemei:")
elements = session.playlist(playlist_id=playlists["items"][num]["id"], fields="tracks(items(track(name)))")

for element in elements["tracks"]["items"]:
    print(element["track"]["name"])