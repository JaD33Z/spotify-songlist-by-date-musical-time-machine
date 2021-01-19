import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "YOUR-SPOTIFY-ID"
CLIENT_SERCRET = "YOUR-SPOTIFY-CLIENT-SECRET-KEY"
billboard_site_url = "https://www.billboard.com/charts/hot-100"


###### SCRAPING BILLBOARD SITE FOR TOP 100 SONGS ACCORDING TO USER DATE INPUT #############
###### ENTER DATE IN YYYY-MM-DD FORMAT WHEN PROMPTED #################################

date_request = input("What year would you like to travel to? Enter date in YYYY-MM-DD format: ")
response = requests.get(url=f"{billboard_site_url}/{date_request}")
billboard_site_info = response.text
soup = BeautifulSoup(billboard_site_info, "html.parser")
song_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.get_text() for song in song_spans]


####### CREATES SPOTIFY AUTHENTICATION ###########

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENT_ID, client_secret=CLIENT_SERCRET,
    show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]

###### SEARCHES SPOTIFY FOR SONGS AND GETS THE TRACK'S URI ###################

song_uris = []
year = date_request.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not listed in Spotify. Skipped.")



####### CREATES YOUR PLAYLIST OF TOP 100 SONGS BY THE DATE YOU ENTERED ############

play_list_create = sp.user_playlist_create(user=user_id, name=f"{date_request} Billboard 100", public=False, collaborative=False, description='')
date_play_list = sp.user_playlist_add_tracks(user=user_id, playlist_id=play_list_create["id"], tracks=song_uris, position=None)
# OR
# date_play_list = sp.playlist_add_items(user_id, play_list_create["id"], song_uris, position=None)
print(date_play_list)






















