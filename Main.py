import tkinter as tk

from pygame import mixer
mixer.init()
mixer.music.load("gamev1.mp3")
mixer.music.play(-1)
root = tk.Tk()

root.title("// GAME HUB //")
root.state("zoomed")
root.config(bg="black")

label = tk.Label(root, text="// GAME HUB //",font=("Impact",75,"bold"),fg="green",bg="black")
label.pack(pady=15)

label = tk.Label(root, text="WELCOME -_- !!",font=("Arial Black",15),bg="black",fg="white")
label.pack(pady=15)

label = tk.Label(root, text="cheen tapaak dum dum !",font=("Arial",10),fg="black")
label.pack(pady=25)


def hover_on(event):
     event.widget.config(
          fg="#39FF14",bg="#111111"
          )
     
def hover_off(event):
     event.widget.config(
          fg="white",
          bg="black"
     )


attempts1=10
attempts2=10
attempts3=10

def guess_game() :
    guessgame=tk.Toplevel(root)
    guessgame.state("zoomed")
    guessgame.config(bg="black")


    label=tk.Label(guessgame,text="/// Welcome To The Game Of Guessing The Number ///",bg="black",font=("Impact",50,"underline"),fg="white")
    label.pack(pady=15)
    label=tk.Label(guessgame,text="--- Select Your Difficulty ---",font=("Arial",25),fg="black")
    label.pack(pady=15)

    info=tk.Label(guessgame,bg="black",fg="#39FF14")
    info.pack_forget()

    prompt=tk.Label(guessgame,bg="black",fg="#39FF14")
    prompt.pack_forget()

    entry=tk.Entry(guessgame)
    entry.pack_forget()

    submit=tk.Button(guessgame,text="Submit")
    submit.pack_forget()

    result=tk.Label(guessgame,bg="black",fg="#39FF14")
    result.pack_forget()

    def easy():
        info.config(text="-Choose between 1 and 10-",font=("Arial",45),fg="red")

        import random
        secret = random.randint(1, 10)
        global attempts1

        prompt.config(text="Enter your guess",font=("Arial",20),fg="grey")
        
        info.pack()
        prompt.pack()
        entry.pack()
        result.pack()
        
        def check1():
            guess=int(entry.get())
            global attempts1
            
            if guess>secret :
                    attempts1 -= 1
                    label.config(text=f"WRONG!!🥲 (Maybe Lower.....)you have {attempts1} attempts left",fg="darkred")

            elif guess<secret :
                    attempts1 -= 1
                    label.config(text=f"WRONG!!🙄 (Maybe Higher..)you have {attempts1} attempts left",fg="darkred")
                    

            if guess == secret:
                label.config(text="YOU WINN!!!🗿🗿",fg="gold") 

        
            if attempts1 == 0:
                label.config(text="YOU LOSE!!!🤣🤣",fg="navyblue")
                
                label.config(text=f"the secret number was {secret}😏",fg="navyblue")
                
        
        if entry =="":
            label.config(text="Enter a number first!")
            return
        
        submit.config(command=check1)
        submit.pack()
        
    

    def medium():
        info.config(text="-Choose between 1 and 50-",font=("Arial",45))
        
        import random
        secret = random.randint(1, 50)
        global attempts2

        prompt.config(text="Enter your guess",font=("Arial",20),fg="grey")
        
        info.pack()
        prompt.pack()
        entry.pack()
        result.pack()


        label=tk.Label(guessgame,text="",bg="black")
        label.pack()

        def check2():
            guess=int(entry.get())
            global attempts2
           
            if guess>secret :
                    attempts2 -= 1
                    label.config(text=f"WRONG!!🥲 (Maybe Lower.....)you have {attempts2} attempts left",fg="darkred")


            elif guess<secret :
                    attempts2 -= 1
                    label.config(text=f"WRONG!!🙄 (Maybe Higher..)you have {attempts2} attempts left",fg="darkred")
                    

            if guess == secret:
                label.config(text="YOU WINN!!!🗿🗿",fg="gold") 
    
            if attempts2 == 0:
                label.config(text="YOU LOSE!!!🤣🤣",fg="navyblue")
                
                label.config(text=f"the secret number was {secret}😏",fg="navyblue")
                
        
        if entry=="":
            label.config(text="Enter a number first!",bg="black",fg="#39FF14")
            return
        
        submit.config(command=check2)
        submit.pack()
    
    def difficult():
        info.config(text="-Choose between 1 and 100-",font=("Arial",45),bg="black")
    
        import random
        secret = random.randint(1, 100)
        global attempts3

        prompt.config(text="Enter your guess",font=("Arial",20),bg="black",fg="grey")
        
        info.pack()
        prompt.pack()
        entry.pack()
        result.pack()

        label=tk.Label(guessgame,text="",bg="black")
        label.pack()

        def check3():
            guess=int(entry.get())
            global attempts3
           
            if guess>secret :
                    attempts3 -= 1
                    label.config(text=f"WRONG!!🥲 (Maybe Lower.....)you have {attempts3} attempts left",fg="darkred")


            elif guess<secret :
                    attempts3 -= 1
                    label.config(text=f"WRONG!!🙄 (Maybe Higher..)you have {attempts3} attempts left",fg="darkred")
                    

            if guess == secret:
                label.config(text="YOU WINN!!!🗿🗿",fg="gold") 
    
            if attempts3 == 0:
                label.config(text="YOU LOSE!!!🤣🤣",fg="navyblue")
                
                label.config(text=f"the secret number was {secret}😏",fg="navyblue")
            
        if entry =="":
            label.config(text="Enter a number first!")
            return
        
        submit.config(command=check3)
        submit.pack()

    border1=tk.Frame(guessgame,bg="#39FF14",padx=1,pady=1)
    border1.pack(pady=15)
    button2=tk.Button(border1,text="EASY",command=easy,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",15,"bold"),width=23,height=1)
    button2.pack()
    button2.bind("<Enter>",hover_on)
    button2.bind("<Leave>",hover_off)

    border2=tk.Frame(guessgame,bg="#39FF14",padx=1,pady=1)
    border2.pack(pady=15)
    button3=tk.Button(border2,text="MEDIUM",command=medium,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",15,"bold"),width=23,height=1)
    button3.pack()
    button3.bind("<Enter>",hover_on)
    button3.bind("<Leave>",hover_off)

    border3=tk.Frame(guessgame,bg="#39FF14",padx=1,pady=1)
    border3.pack(pady=15)
    button4=tk.Button(border3,text="DIFFICULT",command=difficult,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",15,"bold"),width=23,height=1)
    button4.pack()
    button4.bind("<Enter>",hover_on)
    button4.bind("<Leave>",hover_off)
    
    guessgame.mainloop


border1=tk.Frame(root,bg="#39FF14",padx=1,pady=1)
border1.pack(pady=15)
button1 = tk.Button(border1, text="🔢Number Game",command=guess_game,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=30,height=1)
button1.pack()
button1.bind("<Enter>",hover_on)
button1.bind("<Leave>",hover_off)

def rps():
    import random

    rpsgame = tk.Toplevel(root)
    rpsgame.state("zoomed")
    rpsgame.config(bg="black")

    choices = ["rock","paper","scissors"]
    
    result=tk.Label(rpsgame,text="/// Choose between Rock, Paper, Scissors !-_-  ///",bg="black",font=("Impact",50,"underline"),fg="darkgray")
    result.pack(pady=15)
    
    
    def rock():
            user="rock"
            comp_choice = random.choice(choices)
            if user == comp_choice:
                 result.config(text='--- TIE!🙄😤  Computer choice: rock ---',fg="navyblue")
            elif user == "rock" and comp_choice == "scissors" :
                 result.config(text="--- YoU WIN!!😵‍💫🤐   Computer choice: scissors ---",fg="gold")
            elif user=="rock" and comp_choice=="paper":
                 result.config(text="--- You Lose!!🤣😏   Computer choice: paper ---",fg="darkred")
            
    def scissors():
            user="scissors"
            comp_choice = random.choice(choices)
            if user == comp_choice:
                 result.config(text='--- TIE!🙄😤  computer choice: scissors ---',fg="navyblue")
            elif user == "scissors" and comp_choice == "paper" :
                 result.config(text="--- YoU WIN!!😵‍💫🤐   Computer choice: paper ---",fg="gold")
            elif user=="scissors" and comp_choice=="rock":
                 result.config(text="--- You Lose!!🤣😏   Computer choice: rock ---",fg="darkred")

    def paper():
            user="paper"
            comp_choice = random.choice(choices)
            if user == comp_choice:
                 result.config(text='---TIE!🙄😤  Computer choice: paper ---',fg="navyblue")
            elif user == "paper" and comp_choice == "rock" :
                 result.config(text="---YoU WIN!!😵‍💫🤐   Computer choice: rock ---",fg="gold")
            elif user=="paper" and comp_choice=="scissors":
                 result.config(text="---You Lose!!🤣😏   Computer choice: scissors ---",fg="darkred")
    

    result=tk.Label(rpsgame,text="",bg="black",fg="white",font=("Arial",35))
    result.pack(pady=12)
    border1=tk.Frame(rpsgame,bg="#39FF14",padx=1,pady=1)
    border1.pack(pady=15)
    button3=tk.Button(border1,text="ROCK",command=rock,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=20,height=2,)
    button3.pack()
    button3.bind("<Enter>",hover_on)
    button3.bind("<Leave>",hover_off)

    border2=tk.Frame(rpsgame,bg="#39FF14",padx=1,pady=1)
    border2.pack(pady=15)
    button4=tk.Button(border2,text="PAPER",command=paper,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=20,height=2)
    button4.pack()
    button4.bind("<Enter>",hover_on)
    button4.bind("<Leave>",hover_off)

    border3=tk.Frame(rpsgame,bg="#39FF14",padx=1,pady=1)
    border3.pack(pady=15)
    button5=tk.Button(border3,text="SCISSORS",command=scissors,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=20,height=2)
    button5.pack()
    button5.bind("<Enter>",hover_on)
    button5.bind("<Leave>",hover_off)

border2=tk.Frame(root,bg="#39FF14",padx=1,pady=1)
border2.pack(pady=15)

button2= tk.Button(border2, text ="ROCK🪨 PAPER📃 SCISSORS✂️", command=rps,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=30,height=1)
button2.pack()
button2.bind("<Enter>",hover_on)
button2.bind("<Leave>",hover_off)

def calculator():

    calc=tk.Toplevel(root)
    calc.state("zoomed")
    calc.config(bg="black")
    =mixer.Sound(".wav")
    .play()

    label=tk.Label(calc,text="/// Welcome to the calculator ///",bg="black",fg="lime",font=("Impact",50,"bold","underline"))
    label.pack(pady=15)
    label=tk.Label(calc,text="^_^ Enter the first no. :",bg="black",fg="grey",font=("Arial",18))
    label.pack(pady=12)
    entry=tk.Entry(calc)
    entry.pack()
    label=tk.Label(calc,text="^_^ Enter the second no. :",bg="black",fg="grey",font=("Arial",18))
    label.pack(pady=12)
    entry2=tk.Entry(calc)
    entry2.pack()
    result=tk.Label(calc,text="",bg="black",fg="blue",font=("Arial",20))
    result.pack(pady=12)

    label=tk.Label(calc,text="Operation Available:",bg="white",fg="black",font=("Impact",28,"bold","italic"))
    label.pack(pady=15)

    border1=tk.Frame(calc,bg="#39FF14",padx=1,pady=1)
    border1.pack(pady=15)
    add=tk.Button(border1,text="add",command=lambda:result.config(text=f"result = {float(entry.get()) + float(entry2.get())}"),fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",18,"bold"),width=18,height=1)
    add.pack()
    add.bind("<Enter>",hover_on)
    add.bind("<Leave>",hover_off)

    border2=tk.Frame(calc,bg="#39FF14",padx=1,pady=1)
    border2.pack(pady=15)
    subtract=tk.Button(border2,text="subtract",command=lambda:result.config(text=f"result = {float(entry.get()) - float(entry2.get())}"),fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",18,"bold"),width=18,height=1)
    subtract.pack()
    subtract.bind("<Enter>",hover_on)
    subtract.bind("<Leave>",hover_off)

    border3=tk.Frame(calc,bg="#39FF14",padx=1,pady=1)
    border3.pack(pady=15)
    multiply=tk.Button(border3,text="multiply",command=lambda:result.config(text=f"result = {float(entry.get()) * float(entry2.get())}"),fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",18,"bold"),width=18,height=1)
    multiply.pack()
    multiply.bind("<Enter>",hover_on)
    multiply.bind("<Leave>",hover_off)

    border4=tk.Frame(calc,bg="#39FF14",padx=1,pady=1)
    border4.pack(pady=15)
    divide=tk.Button(border4,text="divide",command=lambda:result.config(text=f"result = {float(entry.get()) / float(entry2.get())}"),fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",18,"bold"),width=18,height=1)
    divide.pack()
    divide.bind("<Enter>",hover_on)
    divide.bind("<Leave>",hover_off)

border3=tk.Frame(root,bg="#39FF14",padx=1,pady=1)
border3.pack(pady=15)

button3=tk.Button(border3, text ="🧮CALCULATOR", command=calculator,fg="#39FF14",bg="black",activebackground="black",activeforeground="#39FF14",bd=0,font=("Arial",20,"bold"),width=30,height=1)
button3.pack()
button3.bind("<Enter>",hover_on)
button3.bind("<Leave>",hover_off)

root.mainloop()