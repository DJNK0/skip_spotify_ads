import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import win32gui, win32api, win32con

scope = "user-read-currently-playing" 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope)) #Initialize spotify

def click(x, y):
    hWnd = win32gui.FindWindow(None, "Spotify free") #Window handle
    lParam = win32api.MAKELONG(x, y)
    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    time.sleep(1)
    win32gui.ShowWindow(hWnd, win32con.SW_MAXIMIZE) #Maximize window

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
                    os.startfile('path_to_spotify_executable')
                    time.sleep(2)
                    click(1274, 1345)
    time.sleep(2)
    print("running")
