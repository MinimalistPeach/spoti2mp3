from logic.get_all_playlist import get_all_playlist
from logic.session_creator import create_session
from logic.show_selected_playlist import show_selected_playlist

def main():
    session = create_session()

    playlists = get_all_playlist(session)

    show_selected_playlist(session, playlists=playlists)

if __name__ == "__main__":
    main()