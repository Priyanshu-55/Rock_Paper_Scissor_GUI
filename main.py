#***********  Priyanshu   **********


import random
from tkinter import *

#******************************************
#window screen
mn=Tk()
mn.config(bg='#856ff8')
mn.title("Rock_Paper_Scissor")
mn.maxsize(800,600)
mn.minsize(800,600)
#*****************************************


#label for battle ground
btl=Label(mn,text=" ",bg="black")
btl.place(x=50,y=100,height=100,width=700)

#label for V/S
versus=Label(mn,text="V/S",bg="black",fg="green",font=("Impact",50))
versus.place(x=300,y=100,height=100,width=200)

#user and bot label
usser=Label(mn,text="User",bg='#856ff8',font=("Impact",50))
usser.place(x=50,y=0,height=100,width=200)
bbot=Label(mn,text="Bot",bg='#856ff8',font=("Impact",50))
bbot.place(x=500,y=0,height=100,width=200)



#choices
#user choice
def userchs(usrtext):
    userlabel=Label(mn,text=usrtext,bg="black",fg="red",font=('Brush Script MT', 50))
    userlabel.place(x=50,y=100,height=100,width=250)

#bot choice
def botchs(bottext):
    botchlabel=Label(mn,text=bottext,bg="black",fg="red",font=('Brush Script MT', 50))
    botchlabel.place(x=500,y=100,height=100,width=250)


#counter
bot_wins=0
user_wins=0

#*************************labels*****************************************************

bot_wins_lbl=Label(mn,text=bot_wins,bg='#856ff8',fg="orange",font=('Impact', 60))
user_wins_lbl=Label(mn,text=user_wins,bg='#856ff8',fg="orange",font=('Impact', 60))
bot_wins_lbl.place(x=625,y=450,height=100,width=75)
user_wins_lbl.place(x=125,y=450,height=100,width=75)

#***********************************************************************************

def refresh_win_conter():
    global bot_wins,user_wins
    user_wins_lbl.config(text=user_wins)
    bot_wins_lbl.config(text=bot_wins)

#*********************************reseting the counter****************************
def new_counter():
    global bot_wins,user_wins
    bot_wins=user_wins=0
    refresh_win_conter()

    
#result screen
def resultlabel(reslt):
    reslabel=Label(mn,text=reslt,bg='#856ff8',fg="yellow",font=('Impact', 60))
    reslabel.place(x=200,y=450,height=100,width=400)
    refresh_win_conter()

#******************************bot**************************************************
#guess the response
ls=["Rock","Paper","Scissor"]*3
def rndbot(user):
    global bot_wins,user_wins
    a=random.choice(ls)
    botchs(a)
    if a==user:
        resultlabel("Tie")
        bot_wins+=1
        user_wins+=1
    elif (a=="Rock" and user=="Scissor") or (a=="Paper" and user=="Rock") or (a=="Scissor" and user=="Paper") :
        resultlabel("Bot Wins")
        bot_wins+=1
    else:
        resultlabel("User Wins")
        user_wins+=1
    refresh_win_conter()

#buttons commands
def rckkbtn():
    rndbot("Rock")
    userchs("Rock")

def paprbtn():
    userchs("Paper")
    rndbot("Paper")

def sesrbtn():
    rndbot("Scissor")
    userchs("Scissor")

#**********************************************All Buttons**************************************************************

rckbtn=Button(mn,text="ROCK",command=rckkbtn,bg='#ff3385',font=('Impact', 40),activebackground='#e6005c')
pprbtn=Button(mn,text="PAPER",command=paprbtn,bg='#ff3385',font=('Impact', 40),activebackground='#e6005c')
ssrbtn=Button(mn,text="SCISSOR",command=sesrbtn,bg='#ff3385',font=('Impact', 40),activebackground='#e6005c')
rfrsbtn=Button(mn,text="Refresh",command=new_counter,fg="white",bg="orange",font=('Impact', 40),activebackground='black')
rckbtn.place(x=50,y=300,height=100,width=200)
pprbtn.place(x=300,y=300,height=100,width=200)
ssrbtn.place(x=550,y=300,height=100,width=200)
rfrsbtn.place(x=300,y=10,height=80,width=200)

#************************************************************************************************************************

mn.mainloop()