# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:04:20 2022

@author: mayank
"""


import tekore as tk
CLIENT_ID = '7bb7fa88d2674eba9751423dbb414439'
CLIENT_SECRET = '838746057e514ac0ad5c28ac5e203d1c'
def authorize():
 CLIENT_ID = '7bb7fa88d2674eba9751423dbb414439'
 CLIENT_SECRET = '838746057e514ac0ad5c28ac5e203d1c'
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)