from tkinter import *
from random import *

def main():
    global root, s, jumpingjacks1, jumpingjacks2
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

    moveOne(10)
            

    # Function to update the timer
    # def update_timer(secs, mins):
    #     if secs > 0 or mins > 0:
    #         timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #         countdown = s.create_text(350, 55, text=timeformat, fill="black", font="Arial 16")
    #         # Decrement seconds and minutes
    #         if secs == 0:
    #             mins -= 1
    #             secs = 59
    #         else:
    #             secs -= 1
    #         # Schedule the next update after 1 second
    #         root.after(1000, update_timer, secs, mins)
    #     else:
    #         # Timer has reached 0:00
    #         s.create_text(350, 55, text="00:00", fill="black", font="Arial 16")

    # # Start the timer with 20 seconds
    # update_timer(20, 0)


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
