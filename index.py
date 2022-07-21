import tkinter

app = tkinter.Tk()
app.title("Video Downloader")
app.geometry("400x200")

lb = tkinter.Label(app,text="Do you want to send the video in this directory ? [y/n]").pack

app.mainloop()