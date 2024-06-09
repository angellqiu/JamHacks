from tkinter import *
from random import *

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

    def drawIntro():
        s.create_image(400, 300, image=lobby)
    
    # root.bind("<Button-1>", startScreenClick)
    # def startScreenClick(event):
    drawIntro()


            

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

    # Start the timer with 20 seconds
    workoutTime = randint(15,30)*2
    timer(workoutTime, 0)
    moveOne(workoutTime/2)
    




    # GRIDLINES
    for x in range(50, 850, 25):
        s.create_line(x, 40, x, 650, fill="black")
        s.create_text(x, 20, text=str(x), fill="black", font="Arial 5")
        
    for y in range(50, 650, 25):
        s.create_line(40, y, 850, y, fill="black")
        s.create_text(20, y, text=str(y), fill="black", font="Arial 6")

    root.mainloop()

if __name__ == "__main__":
    main()
