from tkinter import *
from random import randint

#User choice
def the_choice(x):
    if x == "rck":
        rock_user.configure(image=rck)
    elif x == "pap":
        rock_user.configure(image=pap)
    else:
        rock_user.configure(image=scs)
#Computer choice
    choices = ["rck", "pap", "scs"]
    ai_choice = choices[randint(0, 2)]
    if ai_choice == "rck":
        rock_computer.configure(image=rck)
    elif ai_choice == "pap":
        rock_computer.configure(image=pap)
    else:
        rock_computer.configure(image=scs)

    the_winner(x, ai_choice)
        
#Scores

def play_score():
    score = int(play_count["text"])
    score += 1
    play_count["text"] = str(score)


def comp_score():
    score = int(comp_count["text"])
    score += 1
    comp_count["text"] = str(score)

#The winner

def who_won(x):
    winner["text"] = x

def the_winner(player, ai):
    if player == ai:
        who_won("A tie!")
    elif player == "rck":
        if ai == "pap":
            who_won("A.I won!")
            comp_score()
        else:
            who_won("You won!!!")
            play_score()
    elif player == "pap":
        if ai == "scs":
            who_won("A.I won!")
            comp_score()
        else:
            who_won("You won!!!")
            play_score()
    elif player == "scs":
        if ai == "rck":
            who_won("A.I won!")
            comp_score()
        else:
            who_won("You won!!!")
            play_score()

#main window, program's title and an icon, bacground black.

root = Tk()
root.resizable(False, False)
root.title("Rock Paper Scissors!")
root.iconbitmap('my_images/favicon.ico')
root.geometry("720x512")
root.configure(bg='black')

#import the title "Rock paper scissors".

title = PhotoImage(file='my_images/title.png')
my_title = Label(image=title, bg='black')

#import button images

btn1 = PhotoImage(file='my_images/but1.png')
btn2 = PhotoImage(file='my_images/but2.png')
btn3 = PhotoImage(file='my_images/but3.png')

#import images for rock paper scissors vs and user, computer

versus = PhotoImage(file='my_images/vs.png')
rck = PhotoImage(file='my_images/rck.png')
pap = PhotoImage(file='my_images/pap.png')
scs = PhotoImage(file='my_images/scs.png')
user = PhotoImage(file='my_images/user.png')
ai = PhotoImage(file='my_images/pc.png')

#buttons

rock_button = Button(root, image=btn1, bg='black', borderwidth=0, command=lambda:the_choice("rck"))
paper_button = Button(root, image=btn2, bg='black', borderwidth=0, command=lambda:the_choice("pap"))
scissors_button = Button(root, image=btn3, bg='black', borderwidth=0, command=lambda:the_choice("scs"))

#create player rock paper scissors and vs

rock_user = Label(image=rck, bg='black')
vs = Label(image=versus, bg='black')

#create computer rock paper scissors

rock_computer = Label(image=rck, bg='black')

#User and Computer counter, winner announcement

winner = Label(text="Play", bg="black", fg="white", font=40)

the_player = Label(image=user, bg='black')
the_computer = Label(image=ai, bg='black')
play_count = Label(text='0', bg='black', fg='white', font=40)
comp_count = Label(text='0', bg='black', fg='white', font=40)

#all placings

my_title.place(x=60, y=48)
rock_button.place(x=70, y=400)
paper_button.place(x=274, y=400)
scissors_button.place(x=478, y=400)

winner.place(x=332, y=370)

rock_user.place(x=90, y=167)
vs.place(x=270, y=166)
rock_computer.place(x=530, y=167)

the_player.place(x=90, y=283)
the_computer.place(x=530, y=283)

play_count.place(x=136, y=317)
comp_count.place(x=576, y=317)


root.mainloop()