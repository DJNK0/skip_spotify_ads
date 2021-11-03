from configparser import ConfigParser, DuplicateSectionError
import os

current_dir = os.getcwd()

def replace_slashes(string):
    index = 0
    for char in string:
        if char == "\\":
            string = string.replace(char, "/")
            index += 1
        index += 1
    return string

config = ConfigParser()
config.read('config.ini')

try:
    config.add_section('main')
except DuplicateSectionError:
    print("")
config.set('main', 'first_time', 'yes')

print("Enter the path to your spotify executable")
spotify_path = replace_slashes(input())

print("Enter the path to your python interpreter, an then main.py" + "\n")
print("There should be a space in between them and in this exact order, and they should be in between doube qoutes.")

main_py_path = replace_slashes(input())

config.set('main', 'spotify_path', spotify_path)
config.set('main', 'main_py_path', main_py_path)

with open('config.ini', 'w') as f:
    config.write(f)

start_script_bat = open(r'start_script.bat', 'w')
start_script_bat.write(main_py_path + '"\n' + "pause")
start_script_bat.close()

spotify_bat = open(r'spotify.bat', 'w')
spotify_bat.write("@echo off" + "\n" + "START " + spotify_path + "\n" + "call " + current_dir + '"\start_script.bat"')