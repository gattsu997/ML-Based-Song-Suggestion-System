
import authorization
import spotipy
import json
import webbrowser
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

user = spotifyObject.current_user()
print(json.dumps(user,sort_keys=True, indent=4))


while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        searchQuery = input("Enter Song Name: ")
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        tracks_dict = searchResults['tracks']
        p=tracks_dict
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif choice == 0:
        
        
        x=(p["items"][0])
        y=x["id"]
        print(y)
        break
    else:
        print("Enter valid choice.")
        
        


