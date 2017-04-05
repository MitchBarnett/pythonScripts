from datetime import datetime
import time
from threading import Thread
from tkinter import *

root = Tk()

root.title("Beats Clock")

tl = Toplevel()

l = Label(tl, justify=LEFT, text =  "lesson1: @364-@406\n\
Tutor:   @406-@416\n\
Lesson2: @416-@458\n\
Break:   @458-4@75\n\
Lesson3: @475-@517\n\
Lesson4: @517-@559\n\
Lunch:   @559-@590\n\
Lesson5: @590-@631\n", font="Courier 12")
l.pack(side=LEFT)


global var
var = StringVar()
    
def convert():
        while True:
                time.sleep(0.01)
                c = datetime.utcnow()
                h = c.hour + 1
                m = c.minute
                s = c.second
                m += h*60
                s += m*60
                beats = s/86.4
                
                if(beats > 1000):
                        beats = beats - 1000;
                beats_r = round(beats,2)
                var.set('@ '+str(beats_r))


Thread(target = convert).start()
label = Label(textvariable=var)

p = 0
#while True:
#        time.sleep(0.1)
#        print('\n'*60)
#        print('@'+str(round(convert(),1)))
#       p+=1
label.pack()
root.wm_attributes('-topmost', 1)
root.mainloop()
