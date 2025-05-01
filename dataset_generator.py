def sanitize(string: str) -> str: 
    return string.replace('\'', '_').replace('"', '_').replace('[', '_').replace(']', '_').replace(',','_') 

def sanitize_list(list_: list) -> list: 
    sanitized_list = [] 
    for element in list_:
        sanitized_list.append(sanitize(element))
        return sanitized_list # Gather all the unique artist IDs and dump them to a file. 

import pandas as pd 

df_songs = pd.read_csv('data/tracks_features.csv', index_col = 'id') 
artist_ids = [] 
for artists_string in df_songs['artist_ids']: 
    artists = artists_string[2:-2].split("', '") 
    for artist_id in artists: 
        artist_ids.append(artist_id) 
        artist_ids = np.unique(artist_ids) 

with open('artist_ids.txt', 'w') as out_file: 
    for artist in artist_ids: 
        out_file.write(artist + '\n') 

# Use the Spotify API to download information about the artists. 
# Requires Spotify Developer tokens 
import json 
import time 
import spotipy 

CID = '' 
SECRET = '' 
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id = CID, client_secret = SECRET) 
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager) 

with open('artist_ids.txt', 'r') as fin: 
    lines = fin.readlines() 
    lines_n = len(lines) 
    batch_artists = [] 
    for index, line in enumerate(lines):
        artist_id = line.strip() 
        if len(batch_artists) < 50: 
            batch_artists.append(artist_id) 
        else: 
            artists = sp.artists(batch_artists) 
            artists = artists['artists'] 
            for artist in artists: 
                with open(f'artists_dump/{ artist["id"] }.json', 'w') as fout: 
                    fout.write(json.dumps(artist)) 
                    print(f'[ { index + 1 } / { lines_n } ] { artist["id"] } - { artist["name"] }')
                    batch_artists = [] 
                    time.sleep(1)

# Print all the IDs of the artists that are missing from the dump. 
import os 
with open('./artist_ids.txt', 'r') as artist_ids_file: 
    for artist_id in artist_ids_file:
        artist_id = artist_id.strip() 
        artist_file_path = f'./artists_dump/{ artist_id }.json'
        if not os.path.isfile(artist_file_path): 
            print(artist_id) 

# Generate artists dataset
# Read every artist file and generate a CSV file. The category column is not populated yet.
import os 
all_files = [ f for f in os.listdir('./artists_dump/') if os.path.isfile(os.path.join('./artists_dump/', f)) ]
all_artists = { 'id': [], 'name': [], 'genres': [], 'category': [], 'followers': [], 'popularity': [] } 
for current_file in all_files: 
    with open(os.path.join(ARTISTS_DUMP, current_file), 'r') as in_file: 
        artist = json.load(in_file) 
        all_artists['id'].append(artist['id']) 
        all_artists['name'].append( sanitize(artist['name']) )
        all_artists['genres'].append( sanitize_list(artist['genres']) )
        all_artists['category'].append(None)
        all_artists['followers'].append(artist['followers']['total']) 
        all_artists['popularity'].append(artist['popularity']) 
        df_artists = pd.DataFrame(all_artists).set_index('id')
        df_artists.to_csv('artists.csv') 

# Generate genres dataset 
# Iterate through the artists dump, collect every genre and save all unique genres in a file. 
import json 
import os 
import numpy
all_files = [ f for f in os.listdir('./artists_dump/') if os.path.isfile(os.path.join('./artists_dump/', f)) ] 
all_genres = [] 
for current_file in all_files:
    with open(os.path.join(ARTISTS_DUMP, current_file), 'r') as in_file:
        data = json.load(in_file)
        name = data['name'] 
        genres = data['genres'] 
        for genre in genres:
            all_genres.append(genre)
            unique_genres = numpy.unique(all_genres)
            df_genres = pd.DataFrame({ 'genre': unique_genres })
            df_genres['genre'] = df_genres['genre'].apply(sanitize) 
            df_genres.set_index('genre', inplace = True) 
            df_genres.to_csv('genres.csv')
            # Assign categories to every genre
            df_genres = pd.read_csv('genres.csv')
            df_genres['category'] = 'other'
            df_genres.loc[df_genres['genre'].str.contains('disco'), 'category'] = 'disco'
            df_genres.loc[df_genres['genre'].str.contains('metal'), 'category'] = 'metal'
            df_genres.loc[df_genres['genre'].str.contains('rock'), 'category'] = 'rock'
            df_genres.loc[df_genres['genre'].str.contains('classic'), 'category'] = 'classic'
            df_genres.loc[df_genres['genre'].str.contains('punk'), 'category'] = 'punk'
            df_genres.loc[df_genres['genre'].str.contains('jazz'), 'category'] = 'jazz'
            df_genres.loc[df_genres['genre'].str.contains('hip hop'), 'category'] = 'hiphop'
            df_genres.loc[df_genres['genre'].str.contains('electronic'), 'category'] = 'electronic' 
            df_genres.loc[df_genres['genre'].str.contains('pop'), 'category'] = 'pop'
            df_genres.loc[df_genres['genre'].str.contains('k-pop'), 'category'] = 'k-pop'
            df_genres.loc[df_genres['genre'].str.contains('folk'), 'category'] = 'folk'
            df_genres.loc[df_genres['genre'].str.contains('rap'), 'category'] = 'rap'
            df_genres.loc[df_genres['genre'].str.contains('trap'), 'category'] = 'trap'
            df_genres.loc[df_genres['genre'].str.contains('blues'), 'category'] = 'blues'
            df_genres.loc[df_genres['genre'].str.contains('reggae'), 'category'] = 'reggae'
            df_genres.loc[df_genres['genre'].str.contains('reggaeton'), 'category'] = 'reggaeton'
            df_genres = df_genres.set_index('genre') df_genres.to_csv('genres.csv')

# Assign categories to every artist 
df_artists = pd.read_csv('artists.csv', index_col = 'id')
df_genres = pd.read_csv('genres.csv', index_col = 'genre')
df_genres['name'] = df_genres.index
artists_categories = []
for index, artist in df_artists.iterrows():
    if artist['genres'] == '[]':
        artists_categories.append([])
        continue

    artist_genres = artist['genres'][2:-2].split("', '")
    artist_categories = []
    for artist_genre in artist_genres:
        # Lookup category for artist_genre
        artist_genre_category = df_genres.loc[artist_genre]['category']
        artist_categories.append(artist_genre_category)
        artists_categories.append(str(list(np.unique(artist_categories))))
        df_artists['category'] = artists_categories df_artists.to_csv('artists.csv')

# Assign genres, categories and artist's popularity to every song (very slow)
df_songs = pd.read_csv('./data/tracks_features.csv', index_col = 'id')
df_artists = pd.read_csv('artists.csv', index_col = 'id')

# Remove duplicated artists
df_artists = df_artists[~df_artists.index.duplicated(keep = 'first')]
song_genres = []
song_categories = [] 
song_popularities = [] 
for index, song in df_songs.iterrows(): 
    artist_ids = song['artist_ids'][2:-2].split("', '") 
    current_song_genres = [] 
    current_song_categories = [] 
    current_song_popularity = 0 
    for artist_id in artist_ids:
        if not artist_id in df_artists.index: 
            continue

        artist = df_artists.loc[artist_id] 
        artist_genres = artist['genres'][2:-2].split("', '")
        artist_categories = artist['category'][2:-2].split("', '")
        artist_popularity = artist['popularity'] 
        current_song_genres.extend(artist_genres) 
        current_song_categories.extend(artist_categories) 
        current_song_popularity = artist_popularity 
        current_song_genres = str(list(np.unique(current_song_genres)))
        current_song_categories = str(list(np.unique(current_song_categories)))
        song_genres.append(current_song_genres)
        song_categories.append(current_song_categories)
        song_popularities.append(current_song_popularity)
        df_songs['genres'] = song_genres
        df_songs['categories'] = song_categories 
        df_songs['artist_popularity'] = song_popularities
        df_songs.to_csv('songs_extended.csv')

# Assign the date of the first release to every artist (very slow) 
df_songs = pd.read_csv('songs_extended.csv', index_col = 'id')
df_songs['release_date'] = pd.to_datetime(df_songs['release_date'], format = '%Y-%m-%d', errors = 'coerce')
df_artists = pd.read_csv('artists.csv', index_col = 'id')
df_artists.reset_index(inplace = True)
first_songs = [] 
for _, artist in df_artists.iterrows(): 
    artist_id = artist['id'] 
    artist_songs_ = df_songs.loc[df_songs['artist_ids'].str.contains(artist_id)] 
    first_song = None 
    for _, artist_song in artist_songs_.iterrows():
        song_release = artist_song['release_date'] 
        if first_song == None or song_release < first_song: 
            first_song = song_release
            first_songs.append(first_song) 
            df_artists['first_song'] = first_songs
            df_artists.set_index('id', inplace = True)
