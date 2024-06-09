from tkinter import *
from random import *
from pip._vendor import requests
import json

apiKey = "77fc40e265ed864dadd49df59b5c20bf"
city = "Waterloo"
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=metric"

data = requests.get(url).json()
result = data['weather'][0]['description']

def main():
    global root, s, countdown_text
    root = Tk()
    s = Canvas(root, width=800, height=600, background="white")
    s.pack()

    # Load the images
    background = PhotoImage(file="studio.png")
    jumpingjacks1 = PhotoImage(file="jumpingjacks1.png")
    jumpingjacks2 = PhotoImage(file="jumpingjacks2.png")
    pushup1 = PhotoImage(file="pushup1.png")
    pushup2 = PhotoImage(file="pushup2.png")
    sidestretch1 = PhotoImage(file="sidestretch1.png")
    sidestretch2 = PhotoImage(file="sidestretch2.png")
    squat1 = PhotoImage(file="squat1.png")
    squat2 = PhotoImage(file="squat2.png")
    lobby = PhotoImage(file="mainpage.png")

    # def drawIntro():
    #     s.create_image(400, 300, image=lobby)
    
    # # root.bind("<Button-1>", startScreenClick)
    # # def startScreenClick(event):
    # drawIntro()


            

    relations = {
        "jumpingjacks1": jumpingjacks1,
        "jumpingjacks2": jumpingjacks2,
        "pushup1": pushup1,
        "pushup2": pushup2,
        "sidestretch1": sidestretch1,
        "sidestretch2": sidestretch2,
        "squat1": squat1,
        "squat2": squat2,
    }


    s.create_image(400, 300, image=background)
    
    #timer clock
    s.create_rectangle(250, 30, 450, 80, fill="white", outline="black", width=3)

    options = ["jumpingjacks", "pushup", "sidestretch", "squat"]
    exercise = choice(options)


    def deleteImage(image):
        s.delete(image)

    def moveOne(repeat):
        if repeat == 0:
            return        
        jump1 = s.create_image(400, 400, image=relations[exercise + "1"])
        root.after(1000, lambda: deleteImage(jump1))
        root.after(1000, lambda: moveTwo(repeat))

    def moveTwo(repeat):
        jump2 = s.create_image(400, 400, image=relations[exercise + "2"])
        root.after(1000, lambda: deleteImage(jump2))
        root.after(1000, lambda: moveOne(repeat-1))

            
    #Function to update the timer
    countdown_text = s.create_text(350, 55, text="", fill="black", font="Arial 16")

    def timer(secs, mins):
        global countdown_text
        if mins > 0 or secs > 0:
            format = '{:02d}:{:02d}'.format(mins, secs)
            s.itemconfig(countdown_text, text=format)
            if secs == 0:
                if mins > 0:
                    mins -= 1
                    secs = 59
            else:
                secs -= 1
            # Schedule the next update 1 sec later
            root.after(1000, lambda: timer(secs, mins))
        else:
            # Timer end
            s.itemconfig(countdown_text, text="00:00")

    def drawImage():
        s.create_image(400, 400, image=jumpingjacks1)
    
    feedback = ["Whewhhh, good work!", "LOOK AT YOU GO!", "So proud of you!", "Feelin a little sore?", "Feels nice doesn't it?", "YIPEEEE", "Refreshed yet?", "WOOHOOOOOO!"]
    dialogue = choice(feedback)

    def praise():
        global box, encourage
        box = s.create_oval(575,175,725,250, fill = "white", outline = "pink", width = 3)
        encourage = s.create_text(650, 212.5, text=dialogue, fill="black", font="Arial 10")
    
    def deleteText(text, box):
        s.delete(text)
        s.delete(box)

    def weather():
        message = "Waterloo's current forcast is: " + result
        s.create_rectangle(200,175,600,250, fill = "pink", outline = "black", width = 6)
        s.create_text(400, 212.5, text=message, fill="black", font="Arial 10")

    def decision():
        message = "Waterloo's current forcast is: " + result
        banner = s.create_rectangle(200,175,600,250, fill = "pink", outline = "black", width = 6)
        forcast = s.create_text(400, 212.5, text=message, fill="black", font="Arial 10")
    
    goodConditions = ["clear sky", "few clouds", "scattered clouds", "broken clouds", "mist" ]
    def walk():
        s.create_rectangle(200,175,600,250, fill = "pink", outline = "black", width = 6)
        if result in goodConditions:
            s.create_text(400, 212.5, text="It's a good day to go on a walk! Or a jog... whatever floats your boat!", fill="black", font="Arial 10")
        else:
            s.create_text(400, 212.5, text="Hmm, it's unsuitable weather to go outside. Consider some yoga or zen today!", fill="black", font="Arial 10")

    def pigAnimation():
        workoutTime = randint(15,30)*2
        timer(workoutTime, 0)
        moveOne(workoutTime/2)
        root.after((workoutTime)*1000, lambda: drawImage())
        root.after((workoutTime+2)*1000, lambda: praise())
        root.after((workoutTime+7)*1000, lambda: deleteText(encourage, box))
        root.after((workoutTime+10)*1000, lambda: weather())


    pigAnimation()    






    # # GRIDLINES
    # for x in range(50, 850, 25):
    #     s.create_line(x, 40, x, 650, fill="black")
    #     s.create_text(x, 20, text=str(x), fill="black", font="Arial 5")
        
    # for y in range(50, 650, 25):
    #     s.create_line(40, y, 850, y, fill="black")
    #     s.create_text(20, y, text=str(y), fill="black", font="Arial 6")

    root.mainloop()

if __name__ == "__main__":
    main()
