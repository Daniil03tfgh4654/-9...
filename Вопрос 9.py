from random import * 
 
from tkinter import * 
 
def change(): 
     
    canvas.delete("all") 
     
    q = randint(1,350) 
    u = randint(1,350) 
    s = randint(1,350) 
    g = randint(1,350) 
    c = randint(1,350) 
    n = randint(1,350) 
     
    t = randint(1,3) 
     
    if t == 1: 
        square = canvas.create_polygon(q,u,s,g,c,n) 
    elif t == 2: 
        square = canvas.create_rectangle(q,u,s,g) 
    elif t == 3: 
        square = canvas.create_oval(q,u,s,g) 
         
root=Tk() 
root.geometry('500x500') 
 
canvas=Canvas(root, width = 350,height = 350,bg = 'grey') 
canvas.pack() 
 
Button(text='фигура',command=change).pack() 
 
root.mainloop()



