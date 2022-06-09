# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:12:12 2022

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
import authorization
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

mad_world = "3JOVTQ5h8HGFnDdp4VT3MP"
pi=recommend(track_id = mad_world, ref_df = df, sp = sp, n_recs = 1)
c=(pi["id"])
x=c.values[0]
print((x))
