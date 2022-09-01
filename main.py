from tkinter import *
import math

#Constraints
PINK="#e2979c"  #color palletes from color hunt
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME="Courier"
c=0
timer = None
#Functions Space
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    lab1.config(text="Timer⌛")
    lab2.config(text="")


def start_timer():
    global c
    c+=1
    
    work_sec= 25 * 60  #converting 25 min to sec
    s_break_sec = 5 * 60
    l_break_sec = 20 * 60

    #for this section refer timer image
    if c%8==0:   #if rep is multiple of 8 then we need 20 min brake
        count_down(l_break_sec)
        lab1.config(text="Relax🤩",fg=PINK)
    elif c%2==0: #if it's 2nd/4th/6th....rep  then we need 5 min break
        count_down(s_break_sec)
        lab1.config(text="Break😄",fg=RED)
    else:   #if it's 1st/3rd/5th/7th....rep    have to do work
        count_down(work_sec)
        lab1.config(text="Work🤔",fg=GREEN)

    
def count_down(count):
    count_min = math.floor(count/60)  #for sec to min [300sec...296sec will be trated as same i.e 5min]
    count_sec= count % 60  #for remaining sec
    if count_sec<=9:
        count_sec=f"0{count_sec}"
    if count_sec == 0:
        count_sec="00" #dynamic typing
    

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}") #canvas take itemconfig 
    #with(item to be config,what to config)
    if(count>0):
        global timer
        timer=window.after(10,count_down,count-1 ) #takes amount of time it should wait, 
        #calls fn after that time by passing given arguments
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(c/2)):
            mark += "✅"
            lab2.config(text=mark)

#window
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW) #changing background color


#canvas[Widgth] bg,fg
canvas=Canvas(width=500,height=480,bg=YELLOW,highlightthickness=0) #take even numbers
tomato_img=PhotoImage(file='Focus_Timer/tomato.png') #saves image to variable [use [/] in image path]
canvas.create_image(240,256,image=tomato_img) #x,y,image[variable]
timer_text=canvas.create_text(245,250,text="00:00",fill="#FFFDD0",font=("Stardos Stencil",35,"bold"))
canvas.grid(column=1,row=1)

#Creating Label
lab1=Label(text=" Timer⌛",font=(FONT_NAME,70,"bold"),fg=GREEN,bg=YELLOW)
lab1.grid(column=1,row=0)
lab2=Label(bg=YELLOW,fg=RED,font=(FONT_NAME,15))
lab2.grid(column=1,row=2)

#Button
but1=Button(text="Start👆",font=(FONT_NAME,15,"italic"),highlightthickness=0,command=start_timer)
but1.grid(column=0,row=2)
but2=Button(text="Skip⏯",font=(FONT_NAME,15,"italic"),highlightthickness=0,command=reset)
but2.grid(column=2,row=2)

 
window.mainloop()


# Python is strongly, dynamically typed.

# Strong typing means that the type of a value doesn't change in unexpected ways. 
# A string containing only digits doesn't 
# magically become a number, as may happen in Perl. Every change of type requires 
# an explicit conversion.

# Dynamic typing means that runtime objects (values) have a type, as opposed to 
# static typing where variables have a type.