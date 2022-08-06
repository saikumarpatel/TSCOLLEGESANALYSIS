import tkinter as tkinter
window = tkinter.Tk()
for x in range(5):
    for y in range(4):
        frameGrid = tkinter.Frame(master=window,relief=tkinter.RAISED,border=2,background="black")
        frameGrid.grid(row=x, column=y)
        labelGrid = tkinter.Label(master=frameGrid, text=f"Row No. {x}\nColumn No. {y}")
        labelGrid.pack()
window.mainloop()