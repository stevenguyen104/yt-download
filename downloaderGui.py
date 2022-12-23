import sys
import customtkinter
from pytube import YouTube
from tkinter import *
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

application_path = os.path.dirname(sys.executable)

#button for download mp3
def downloadAudio(link, path):
    print("Audio")
    yt = YouTube(link.get())
# take only audio
    yd = yt.streams.filter(only_audio=True).first()
#download
#if empty, def
    if not path != "":
        destination = path.get()
    else:
        destination = os.path.expanduser("~")+"/Downloads/"
    
    # print(destination)

    downloaded_file = yd.download(output_path=destination)
# remove mp4
    base, ext = os.path.splitext(downloaded_file)
# turn into mp3
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)


def downloadVideo(link, path):
    print("Video")
    yt = YouTube(link.get())
    yd = yt.streams.get_highest_resolution()
    if not path:
        destination = path.get()
    else:
        destination = os.path.expanduser("~")+"/Downloads/"
    
    # print(destination)

    yd.download(output_path=destination)


# gui
root = customtkinter.CTk()
root.title("Video Downloader")
root.geometry("300x300")

s = customtkinter.CTkLabel(root, text="Insert link below:")
s.pack(pady="10")

e = customtkinter.CTkEntry(root, width=150)
e.pack()

label = customtkinter.CTkLabel(root, text="Insert path below:")
label.pack(pady="10")

en = customtkinter.CTkEntry(root, width=150, placeholder_text="Default: /Downloads/")
en.pack()

myButton = customtkinter.CTkButton(root,text="Download as mp3", command=lambda: downloadAudio(e, en))
myButtonTwo = customtkinter.CTkButton(root,text="Download as mp4", command=lambda: downloadVideo(e, en))
myButton.pack(pady="20")
myButtonTwo.pack(pady="10")

root.mainloop()