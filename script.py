from mutagen.id3 import ID3, ID3NoHeaderError
import os , sys
import json
#dir = -1 ;
def File_show (path):
    global dir
    out_path = -1
    in_dir = os.listdir(path)
    for i in in_dir:
        if os.path.isdir(path + i) and  i != "Music":
            print("It is the dir "+ os.path.abspath(path+i)+'\\')
            File_show(os.path.abspath(path+i) +'\\')
        elif i == "Music" and os.path.isdir(path + i):
            dir = path + i
#next def
def getTagsToTxt(path,file):
    files = os.listdir(path)
    music = list(filter(lambda x: x.endswith('.mp3'), files))
    for i in music:
        song_dict = {}
        song_dict['path']= path+i
        print(path+i)
        try:
            audio = ID3(path + "/" + i)
        except ID3NoHeaderError:
            print(None)
            print()
            continue
        try:
            print(audio['TPE1'].text[0])
            song_dict['name'] = audio['TPE1'].text[0]
        except KeyError:
            print(None)
        try:
            print(audio["TIT2"].text[0])
            song_dict['track'] = audio["TIT2"].text[0]
        except KeyError:
            print(None)
        try:
            print(audio["TALB"].text[0])
            song_dict['album'] = audio["TALB"].text[0]
        except KeyError:
            print(None)
        print()
        file.write(json.dumps(song_dict))
        print(json.dumps(song_dict))
        print()
file = open ("playlist.json","w")
#start_dir = input()
start_dir = "/media"
#start_dir = input()
File_show(start_dir)
print (dir)
getTagsToTxt(dir,file)
file.close()
