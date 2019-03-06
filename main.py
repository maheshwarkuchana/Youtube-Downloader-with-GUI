import youtube_dl
import tkinter as tk
from tkinter import ttk

class Downloader(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Youtube Video Downloader")
        self.geometry("400"+"x"+"100")
        self.entry = tk.Entry(self, width=50)#.place(relx=0.2, rely=0.3)
        self.button = tk.Button(self, text="Download", command=self.on_button)#.place(relx=0.45, rely=0.5)
        self.label = tk.Label(self, text="Enter URL ")#.place(relx=0.07, rely=0.3)
        self.button.place(relx=0.45, rely=0.5)#pack()
        self.label.place(relx=0.07, rely=0.3)#pack()
        self.entry.place(relx=0.2, rely=0.3)#pack()
        self.pb = ttk.Progressbar(self, orient='horizontal', length=100, mode='determinate')
        self.pb.pack()

    def dwl(self, txt):
        ydl_opts = {}
        self.pb.start()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([txt])
        self.pb.stop()

    def on_button(self):
        url = self.entry.get()
        print(url)
        txt = url.strip()
        self.dwl(txt)

app = Downloader()
app.mainloop()