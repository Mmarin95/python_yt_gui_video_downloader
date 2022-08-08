# import required libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube


def create_widgets():
    # creating the url label
    link_label = Label(root, text='Paste URL: ', bg="#999999")
    # placing the label
    link_label.grid(row=1, column=0, pady=10, padx=10)

    # creating the url input
    root.link_text = Entry(root, width=60, textvariable=video_link)
    # placing the point
    root.link_text.grid(row=1, column=1, pady=10, padx=10)

    # create audio/video dropdown
    OPTS = ["Video", "Audio"]
    type_of_download.set(OPTS[0])
    root.av_dropdown = OptionMenu(root, type_of_download, *OPTS)
    root.av_dropdown.config(bg="#ffffff")
    # place audio/video dropdown
    root.av_dropdown.grid(row=1, column=2, pady=10, padx=10)

    # creating the destination label
    destination_label = Label(root, text='Destination: ', bg="#999999")
    # placing the label
    destination_label.grid(row=2, column=0, pady=10, padx=10)

    # creating the destination input
    root.destination_label = Entry(root, width=60, textvariable=download_path)
    # placing the box
    root.destination_label.grid(row=2, column=1, pady=10, padx=10)

    # create the browse destination button
    browse_but = Button(root, text="Browse", command=browse_destination, width=10, bg="#ffffff")
    # place the button
    browse_but.grid(row=2, column=2, pady=10, padx=10)

    # create a download button
    download_but = Button(root, text="Download", command=download_video, width=15, bg="#ff0000")
    # place the button
    download_but.grid(row=3, column=1, pady=3, padx=3)


# define browse button function
def browse_destination():
    # set directory
    download_dir = filedialog.askdirectory()
    download_path.set(download_dir)


# create youtube video download function
def download_video():
    url = video_link.get()
    folder = download_path.get()
    get_video = YouTube(url)

    if type_of_download.get() == "Video":
        get_stream = get_video.streams.get_highest_resolution()
    else:
        get_stream = get_video.streams.get_audio_only()

    get_stream.download(folder)

    messagebox.showinfo("Your video is downloaded successfully.")


# creating an instance
root = tk.Tk()

# size of the window
root.geometry("600x130")
root.resizable(False, False)
# name of the window
root.title("Youtube Downloader")
# colors of the window
root.config(background="#999999")

video_link = StringVar()
download_path = StringVar()
type_of_download = StringVar()

create_widgets()

root.mainloop()
