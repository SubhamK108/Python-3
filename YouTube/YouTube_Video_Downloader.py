import os
os.system('clear')
print('MADE BY - Subham Karmakar\n')
from pytube import YouTube
link = input('Enter your Link : \n')
v = YouTube(link)
reso = str(input('Enter the Resolution (Like - 480p, 720p, 2160p ) : '))
frame = int(input('Enter the FPS (30, 60) : '))
direc = str(input('[Only For Windows]Enter the Drive Letter where you want to Save (Like - D:/, E:/) : '))
s = v.streams.filter(res = reso, fps = frame).first()
print(f'Downloading {v.title} ...')
s.download(direc)
print(f'{v.title} has successfully downloaded')
input('Press any key to Exit... ')
