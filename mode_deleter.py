import os
import sys

def GetArgs():
    args = list()
    for i, arg in enumerate(sys.argv):
        args.append(str(arg))
    return args

args = GetArgs()
PATH = os.getcwd()
if len(args) > 2:
    PATH = args[2]
MODES = args[1].split(";")

def RemoveSong(file_path, song_file):
    os.remove(file_path)
    print(f"{song_file} Has been deleted!")


def DeleteSelectedOsuModes(osu_songs_path, modes):
    song_names = os.listdir(osu_songs_path)
    for song_name in song_names:
        if ".py" not in song_name: 
            song_path = osu_songs_path+"\\"+song_name
            song_files = os.listdir(song_path)
            for song_file in song_files:
                if ".osu" in song_file:
                    file_path=song_path+"/"+song_file
                    with open(file_path, "r", encoding="utf8") as file:
                        for line in file.readlines(): 
                            if "Mode: " in line:
                                mode=line.split(":")[1].strip()
                                file.close()
                                if mode not in modes:
                                    RemoveSong(file_path, song_file)
                                
                                
DeleteSelectedOsuModes(PATH, MODES)
