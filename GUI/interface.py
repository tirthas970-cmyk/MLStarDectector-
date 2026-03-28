import tkinter as tk 




actions = ["Detect Star", "Get star info"]


root = tk.Tk()
root.geometry("1920x1080")
bg = tk.PhotoImage(file="C:/Users/peach/Downloads/pexels-felix-mittermeier-956981.png")


canvas1 = tk.Canvas( root, width = 1920,
                 height = 1200)

canvas1.pack(fill = "both", expand = True)


canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

canvas1.create_text(960,50, text="Star-GPT", fill="#FFBE46", font=('Helvetica', 50))
choice = tk.StringVar()
choice.set("What should I do?")
def buttonstate():
    buttonA["state"] = "disabled"
    guess["state"] = "disabled"


guess = tk.OptionMenu(root,choice, *actions, )
guess.config(width= 20, height= 5, font=('Helvetica', 12) )
guess_canvas = canvas1.create_window( 1000, 900, 
    anchor = "nw",
    window = guess)



buttonA = tk.Button(root, text="Confirm", height=5, width=20, activebackground="#FF0000", command=buttonstate)
buttonA_canvas = canvas1.create_window( 450, 900, 
    anchor = "nw",
    window = buttonA)

def quit():
    root.destroy()

buttonQ = tk.Button(root, text="Quit", height=3, width=10, activebackground="#FF0000", command=quit)
buttonQ_canvas = canvas1.create_window( 1800, 0, 
    anchor = "nw",
    window = buttonQ)


root.mainloop()