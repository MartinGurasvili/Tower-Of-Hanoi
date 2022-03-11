import tkinter
from tkinter import *
from PIL import ImageTk,Image
import time

root = Tk()
root.title("Tower Of Hanoi")
root.minsize(width=600, height=450)
root.attributes("-alpha", 0.9)
root.configure(background="#9AD0EC")

title = Label(root, text='Tower Of Hanoi', fg="white",font="Helveca 30",bg="#9AD0EC")
title.pack()

movescount=0

def elem_start_pos():
    global img1,img2,img3,img4,movescount,all_posx,all_posy,canvas,pole,moves
    all_posx=[]
    all_posy=[]
    
    moves = Label(root, text=f'{movescount} Moves', fg="white",font="Helveca 20",bg="#9AD0EC")
    moves.place(relx=0.5, rely=0.12, anchor=CENTER)

    canvas = Canvas(root, width =550, height = 350,background="#9AD0EC",bd=0, highlightthickness=0)  
    canvas.place(relx=0.5, rely=0.55, anchor=CENTER)

    pole = ImageTk.PhotoImage(Image.open("poles.png"))
    canvas.create_image(-20, -20, anchor=NW, image=pole)
    
    restart_game = Button(root,text ="Restart", fg="white", font="Helveca 30 bold",bg='white',activebackground='white',highlightbackground="#71cad3",justify=CENTER,command=lambda:restart_tower_game(),width=13,bd=0)
    restart_game.configure(bg='#85F4FF')
    restart_game.place(relx=0.5,rely=0.92, anchor=SE)

    enter = Button(root,text ="Start", fg="white", font="Helveca 30 bold",bg='white',activebackground='white',highlightbackground="#71cad3",justify=CENTER,command=lambda:TowerOfHanoi(4 , 0, 360, 180),width=13,bd=0)
    enter.configure(bg='#85F4FF')
    enter.place(relx=0.5, rely=0.92, anchor=SW)

    img1 = ImageTk.PhotoImage(Image.open("1.png"))
    all_posx.append(10)
    all_posy.append(0)
    canvas.create_image(all_posy[0], all_posx[0], anchor=NW, image=img1)

    img2 = ImageTk.PhotoImage(Image.open("2.png"))
    all_posx.append(55)
    all_posy.append(0)
    canvas.create_image(all_posy[1], all_posx[1], anchor=NW, image=img2)

    img3 = ImageTk.PhotoImage(Image.open("3.png"))
    all_posx.append(100)
    all_posy.append(0)
    canvas.create_image(all_posy[2], all_posx[2], anchor=NW, image=img3)

    img4 = ImageTk.PhotoImage(Image.open("4.png"))
    all_posx.append(145)
    all_posy.append(0)
    canvas.create_image(all_posy[3], all_posx[3], anchor=NW, image=img4)    

def TowerOfHanoi(n , source, destination, auxiliary):
    global moves,movescount
    if n==1:
        movescount+=1
        moves.configure(text=str(movescount) +" Moves")
        time.sleep(0.4)
        move(0,destination)
        time.sleep(0.4)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    movescount+=1
    moves.configure(text=str(movescount) +" Moves")
    time.sleep(0.4)
    move(n-1,destination)
    time.sleep(0.4)
    TowerOfHanoi(n-1, auxiliary, destination, source)

def move(item,destination):
    global img1,img2,img3,img4
    
    if(item ==0):
        
        if(all_posy[0]!=destination):
            img1 = ImageTk.PhotoImage(Image.open("1.png"))
            canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img1)
            all_posy[0]=destination
            all_posx[0]=145-(45*all_posy.count(destination))
            Tk.update(root) 
            return
    
    elif(item ==1):
        
        if(all_posy[1]!=destination):
            img2 = ImageTk.PhotoImage(Image.open("2.png"))
            canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img2)
            all_posy[1]=destination
            all_posx[1]=145-(45*all_posy.count(destination))
            Tk.update(root) 
            return
    
    elif(item ==2):
        
        if(all_posy[2]!=destination):
            img3 = ImageTk.PhotoImage(Image.open("3.png"))
            canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img3)
            all_posy[2]=destination
            all_posx[2]=145-(45*all_posy.count(destination))
            Tk.update(root) 
            return
    else:
        if(all_posy[3]!=destination):
            img4 = ImageTk.PhotoImage(Image.open("4.png"))
            print(all_posx.count(destination))
            canvas.create_image(destination, 145-(45*all_posy.count(destination)), anchor=NW, image=img4)
            all_posy[3]=destination
            all_posx[3]=145-(45*all_posy.count(destination))
            Tk.update(root) 
            return

def restart_tower_game():
    global img1,img2,img3,img4,all_posx,all_posy,movescount
    movescount=0
    Label.destroy(moves)
    elem_start_pos()

elem_start_pos()
root.mainloop()