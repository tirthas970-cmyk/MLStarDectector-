import tkinter as tk 




actions = ["Detect Star", "Get star info"]


root = tk.Tk()
root.geometry("1920x1080")
bg = tk.PhotoImage(file="C:/Users/peach/Downloads/pexels-felix-mittermeier-956981.png")


canvas1 = tk.Canvas( root, width = 1920,height= 1200)

canvas1.pack(fill = "both", expand = True)


canvas1.create_image( 0, 0, image = bg, anchor = "nw")

title = canvas1.create_text(960,50, text="Star-GPT", fill="#FFBE46", font=('OCR A Extended', 50))
choice = tk.StringVar()
choice.set("What should I do?")

# def guessing():
#     if choice.get() == "Detect Star":
Questions = tk.Toplevel(root)
Questions.title("info")
Questions.geometry("900x600")
Questions.transient(root)
bg2 = tk.PhotoImage(file="C:/Users/peach/Downloads/HuGGeENt6kGyixe3hT9tnY.png")
Questions.withdraw()

# Questions.withdraw()


def buttonstate():
    if choice.get() == "What should I do?":
        print("easter egg")
    else:
        buttonA["state"] = "disabled"
        acts["state"] = "disabled"
        if choice.get() == "Detect Star":
            Questions.deiconify()
            Questions.transient(root)
    # guessing()
    # Questions = tk.Toplevel(root)
    # Questions.title("info")
    # Questions.geometry("200x200")
    # Questions.transient(root)

def  placeholder():
  print("predict")
  # put something here!!!!!!!!!

acts = tk.OptionMenu(root,choice, *actions, )
acts.config(width= 30, height= 5, font=('OCR A Extended', 16) )
acts_canvas = canvas1.create_window( 800, 550, 
    anchor = "nw",
    window = acts)



buttonA = tk.Button(root, text="Confirm", height=5, width=25, activebackground="#FF0000", command=buttonstate, font=('OCR A Extended', 16))
buttonA_canvas = canvas1.create_window( 450, 550, 
    anchor = "nw",
    window = buttonA)

def quit():
    root.destroy()

buttonQ = tk.Button(root, text="Quit", height=3, width=12, activebackground="#FF0000", command=quit, font=('OCR A Extended', 12))
buttonQ_canvas = canvas1.create_window( 1800, 0, 
    anchor = "nw",
    window = buttonQ)

dist_var=tk.StringVar()
lumi_var=tk.StringVar()
radi_var=tk.StringVar()
temp_var=tk.StringVar()

dist = dist_var.get()
lumi = lumi_var.get()
radi = radi_var.get()
temp = temp_var.get()

dist_var.set("")
lumi_var.set("")
radi_var.set("")
temp_var.set("")

canvas2 = tk.Canvas( Questions, width = 1920,height= 1200,)
canvas2.create_image( 0, 0, image = bg2, anchor = "nw")
canvas2.pack(fill = "both", expand = True)


# distL = tk.Label(Questions, text="What is the distance of this star from the earth?", foreground="#FFBE46", font=('OCR A Extended',20,'normal'))
# lumiL = tk.Label(Questions, text="What is the luminosity of this star?", foreground="#FFBE46", font=('OCR A Extended',20,'normal'),)
# radiL = tk.Label(Questions, text="What is the radius of this star?",foreground="#FFBE46", font=('OCR A Extended',20,'normal'))
# tempL = tk.Label(Questions, text="What is the temperature of this star?",foreground="#FFBE46", font=('OCR A Extended',20,'normal') )

distL = canvas2.create_text(450,20, text="What is the distance of this star from the earth?", fill="#FFBE46", font=('OCR A Extended', 20))
lumiL = canvas2.create_text(350,120, text="What is the luminosity of this star?", fill="#FFBE46", font=('OCR A Extended',20,'normal'))
radiL = canvas2.create_text(350,220, text="What is the radius of this star?",fill="#FFBE46", font=('OCR A Extended',20,'normal'))
tempL = canvas2.create_text(350,320, text="What is the temperature of this star?",fill="#FFBE46", font=('OCR A Extended',20,'normal') )


distE = tk.Entry(Questions,textvariable = dist_var, font=('OCR A Extended',20,'normal'))
lumiE = tk.Entry(Questions,textvariable = lumi_var, font=('OCR A Extended',20,'normal'))
radiE = tk.Entry(Questions,textvariable = radi_var, font=('OCR A Extended',20,'normal'))
tempE = tk.Entry(Questions,textvariable = temp_var, font=('OCR A Extended',20,'normal'))



dist2_canvas = canvas2.create_window( 0, 70, anchor = "nw", window = distE)
lumi2_canvas = canvas2.create_window( 0, 170, anchor = "nw", window = lumiE)
radi2_canvas = canvas2.create_window( 0, 270, anchor = "nw", window = radiE)
temp2_canvas = canvas2.create_window( 0, 370, anchor = "nw", window = tempE)

buttonP = tk.Button(Questions, text="Run Analysis", height=5, width=15, activebackground="#FF0000", command=placeholder, font=('OCR A Extended', 12))
buttonP_canvas = canvas2.create_window( 320, 500, 
    anchor = "nw",
    window = buttonP)



root.mainloop()