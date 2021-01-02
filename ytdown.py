import tkinter as tk
import tkinter.font as tkFont
import pytube

def download(url, res):
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.get_by_resolution(resolution = res)
        print("Download Started")
        video.download(output_path="../Video", filename = "myvideo")
        print("Download Done")

    except:
        print("Please give INput")


def start():
    root = tk.Tk()
    root.title("YT Dowloader")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+%d+%d" % (w/2, h/2, w/4, h/4))

    fontStyle = tkFont.Font(family="Lucida Grande", size=20)

    label = tk.Label(root, text="YouTube Video Downlaod", font=fontStyle)
    label.pack(padx=20, pady=10)

    urlInput = tk.Entry(root, font = ("Lucida Grande",18,""), width = "30")
    urlInput.pack(padx=20, pady=10)

    tkvar = tk.StringVar(root)

    choices = {"360p", "480p", "720p", "1080p"}
    tkvar.set("360p")

    popupmenu = tk.OptionMenu(root, tkvar, *choices)
    tk.Label(root, text = "Choose a Resolutiion" ).pack()
    popupmenu.pack()

    submit = tk.Button(root, text="Submit", font=("Lucida Grande",12,"bold"), command=lambda : download(urlInput.get(),tkvar.get()))

    submit.pack(padx=20, pady=5)

    root.mainloop()


if __name__ == "__main__":
    start()
