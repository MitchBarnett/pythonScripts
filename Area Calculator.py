from tkinter import *

def centerWindow(windowName):
    windowName.update()
    # The following creates the main window
    # sets it's size and title
    w = windowName.winfo_width() 
    h = windowName.winfo_height() 
    ws = windowName.winfo_screenwidth()
    hs = windowName.winfo_screenheight()

    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    #This is responsible for setting the dimensions of the screen and where it is
    #placed
    windowName.geometry('%dx%d+%d+%d' % (w, h, x, y))

def calcArea():
    try:
        result.set("Area: " + str(float(widthEntry.get()) * float(heightEntry.get())))
    except:
        result.set("Invalid input")

#Set up window
mainWindow = Tk();
mainWindow.geometry('200x100');
mainWindow.title("Area Calc");
centerWindow(mainWindow);
#mainWindow.resizable(0, 0) # Stops the user being able to resize the window
centerWindow(mainWindow);

result = StringVar()
result.set("Result: ")
widthLabel = Label(mainWindow, text="Width:")
heightLabel = Label(mainWindow, text="Height:")
resultLabel = Label(mainWindow, text="Result:", textvariable=result)
submitButton = Button(mainWindow, text ="Calculate", command = calcArea)

widthEntry = Entry(mainWindow);
heightEntry = Entry(mainWindow);


widthLabel.grid(row = 0, column = 0,sticky = W)
heightLabel.grid(row = 1,column =0,sticky = W)
widthEntry.grid(row = 0,column =1,sticky = W);
heightEntry.grid(row = 1,column =1,sticky = W);
submitButton.grid(row = 2, column = 0,sticky = W)
resultLabel.grid(row = 3, column = 0, columnspan=2, sticky = W)

# MainLoop
mainWindow.mainloop()

