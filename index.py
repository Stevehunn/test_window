from cgitb import text
import tkinter as tk

app = tk.Tk()
app.title("Video Downloader")
canvas = tk.Canvas (app, width=400, height=200, background="purple")
canvas.pack(fill="both",expand=True)

message = tk.Label(app, text="Do you want to send the video in this directory ?")
messageUrl =message
messageUrlResponse =messageUrl
answer_yes = message
answer_no =answer_yes

def action_bouton_yes():
    #phase 1
    canvas.delete("all")
    message.destroy()

    #phase 2

    return
    
def action_bouton_no():
    #phase 1
    canvas.delete("all")
    message.destroy()

    #phase 2
    message2 = tk.Label(app, text="Where do you want to put the video ?")
    message2.pack()
    message2.place(x=80, y= 50)
    answer_yes.destroy()
    answer_no.destroy()

    return

def phase0hide():
    message.destroy()
    messageUrl.destroy()
    messageUrlResponse.destroy()
    answer_yes.destroy()
    answer_no.destroy()
    
    return

def phase1hide():
    buttonWelcome.destroy()
    welcomeButton.destroy()
    messageUrl.destroy()
    messageUrlResponse.destroy()
    return



phase0hide()
#Init
welcomeButton = tk.Label(app, text="Welcome to this video downlaoder app")
welcomeButton.pack()
welcomeButton.place(x=50, y= 50)

buttonWelcome = tk.Button(app , text= "Yes", command=phase1hide)
buttonWelcome.pack()
buttonWelcome.place(x= 100, y=100)


#Phase 1
message = tk.Label(app, text="Do you want to send the video in this directory ?")
message.pack()
message.place(x=50, y= 50)

answer_yes = tk.Button(app , text= "Yes", command=action_bouton_yes)
answer_yes.pack()
answer_yes.place(x= 100, y=100)

answer_no = tk.Button(app , text= "No", command=action_bouton_no)
answer_no.pack()
answer_no.place(x= 250, y=100)

#Phase 2
messageUrl = tk.Label(app, text="Enter the Youtube-url")
messageUrl.pack()
messageUrl.place(x=50, y= 50)

messageUrlResponse = tk.Entry(app, text="truc")
messageUrlResponse.place(x=50, y= 100)





#Quit button
close_app = tk.Button(app , text= "Quit", command= app.quit)
close_app.pack()
close_app.place(x= 360, y=170)

app.mainloop()