import spotipy
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials

def create_session():

    env = dotenv_values("./config/.env")

    CLIENT_ID = env["CLIENT_ID"]
    CLIENT_SECRET = env["CLIENT_SECRET"]

    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET
    )

    session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return session