__author__ = "David Kampmeier"
__license__ = "MIT"
__version__ = "1.0"

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import win32gui, win32api, win32con
from configparser import ConfigParser, DuplicateSectionError

current_dir = os.getcwd()
config = ConfigParser()
config.read(current_dir + '\config.ini')

scope = "user-read-currently-playing" 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope)) #Initialize spotify
spotify_path = config.get('main', 'spotify_path')

def click(x, y):
    hWnd = win32gui.FindWindow(None, "Spotify free") #Window handle
    lParam = win32api.MAKELONG(x, y)
    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    time.sleep(1)
    win32gui.ShowWindow(hWnd, win32con.SW_MAXIMIZE) #Maximize window to get the correct clicking coordinates 

    #Click the coordinates on the specified window
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

while True:
    songplaying = sp.currently_playing() 
    if songplaying: 
        for key in songplaying: #Loop over all keys in songplaying
            if key == "currently_playing_type":
                if songplaying[key] == "ad": #Restart spotify and click button to unpause if ad is playing
                    os.system("TASKKILL /F /IM Spotify.exe")
                    time.sleep(1)
                    os.startfile(spotify_path)
                    time.sleep(2)
                    click(1274, 1345)
    time.sleep(2)
    print("running")
