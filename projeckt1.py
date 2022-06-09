
import json
import spotipy
import webbrowser
username = 'Your_Username'
clientID = '7bb7fa88d2674eba9751423dbb414439'
clientSecret = '838746057e514ac0ad5c28ac5e203d1c'
redirectURI = 'http://google.com/'
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
global y
user = spotifyObject.current_user()
#print(json.dumps(user,sort_keys=True, indent=4))
while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Get a similar song recommendation !!!")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        try:
            searchQuery = input("Enter Song Name: ")
            searchResults = spotifyObject.search(searchQuery,1,0,"track")
            tracks_dict = searchResults['tracks']
            p=tracks_dict
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            webbrowser.open(song)
            print('Song has opened in your browser.')
        except:
            print("try again with cor !!!")
    elif choice == 0:
        x=(p["items"][0])
        y=x["id"]
        print("song opened in browser")
        break
    else:
        print("Enter valid choice.")
        break
import sys
sys.path.append("../spotify_api_web_app")
import authorization
import pandas as pd
from tqdm import tqdm
import time
sp = authorization.authorize()
import pandas as pd
import random
import authorization # this is the script we created earlier
import numpy as np
from numpy.linalg import norm
sp = authorization.authorize()
df = pd.read_csv("valence_arousal_dataset.csv")
df["mood_vec"] = df[["valence", "energy"]].values.tolist()
def recommend(track_id, ref_df, sp, n_recs ):
    
    track_features = sp.track_audio_features(track_id)
    track_moodvec = np.array([track_features.valence, track_features.energy])
    
    ref_df["distances"] = ref_df["mood_vec"].apply(lambda x: norm(track_moodvec-np.array(x)))
    ref_df_sorted = ref_df.sort_values(by = "distances", ascending = True)
    ref_df_sorted = ref_df_sorted[ref_df_sorted["id"] != track_id]
    
    return ref_df_sorted.iloc[:n_recs]

mad_world = y
pi=recommend(track_id = mad_world, ref_df = df, sp = sp, n_recs = 1)
c=(pi["id"])
x=c.values[0]
url="https://open.spotify.com/track/"+ x
webbrowser. open(url)
