# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:12:14 2022

@author: mayank
"""

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

genres = sp.recommendation_genre_seeds()

n_recs = 1

data_dict = {"id":[], "genre":[], "track_name":[], "artist_name":[],
             "valence":[], "energy":[]}


for g in tqdm(genres):
    
    recs = sp.recommendations(genres = [g], limit = n_recs)
    recs = eval(recs.json().replace("null", "-999").replace("false", "False").replace("true", "True"))["tracks"]
    
    for track in recs:
        data_dict["id"].append(track["id"])
        data_dict["genre"].append(g)
        
        track_meta = sp.track(track["id"])
        data_dict["track_name"].append(track_meta.name)
        data_dict["artist_name"].append(track_meta.album.artists[0].name)
        track_features = sp.track_audio_features(track["id"])
        data_dict["valence"].append(track_features.valence)
        data_dict["energy"].append(track_features.energy)
        
        time.sleep(0.2)
        

df = pd.DataFrame(data_dict)

df.drop_duplicates(subset = "id", keep = "first", inplace = True)
df.to_csv("valence_arousal_dataset.csv", index = False)

def distance(p1, p2):
    distance_x = p2[0]-p1[0]
    distance_y = p2[1]-p1[1]
    distance_vec = [distance_x, distance_y]
    norm = (distance_vec[0]**2 + distance_vec[1]**2)**(1/2)
    return norm


df = pd.read_csv("valence_arousal_dataset.csv")
df["mood_vec"] = df[["valence", "energy"]].values.tolist()

sp = authorization.authorize()

def recommend(track_id, ref_df, sp, n_recs = 5):
    
    track_features = sp.track_audio_features(track_id)
    track_moodvec = np.array([track_features.valence, track_features.energy])
    
    ref_df["distances"] = ref_df["mood_vec"].apply(lambda x: norm(track_moodvec-np.array(x)))
    ref_df_sorted = ref_df.sort_values(by = "distances", ascending = True)
    ref_df_sorted = ref_df_sorted[ref_df_sorted["id"] != track_id]
    
    return ref_df_sorted.iloc[:n_recs]
'''
mad_world = "3JOVTQ5h8HGFnDdp4VT3MP"
p=recommend(track_id = mad_world, ref_df = df, sp = sp, n_recs = 5)
print(p)
'''
