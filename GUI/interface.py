import tkinter as tk 




actions = ["Detect Star", "Get star info"]


root = tk.Tk()
root.geometry("1920x1080")
bg = tk.PhotoImage(file="C:/Users/peach/Downloads/pexels-felix-mittermeier-956981.png")


canvas1 = tk.Canvas( root, width = 1920,height= 1200)

canvas1.pack(fill = "both", expand = True)


canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

canvas1.create_text(960,50, text="Star-GPT", fill="#FFBE46", font=('Helvetica', 50))
choice = tk.StringVar()
choice.set("What should I do?")

# def guessing():
#     if choice.get() == "Detect Star":
Questions = tk.Toplevel(root)
Questions.title("info")
Questions.geometry("900x600")
Questions.transient(root)
Questions.withdraw()

# Questions.withdraw()









def buttonstate():
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


acts = tk.OptionMenu(root,choice, *actions, )
acts.config(width= 20, height= 5, font=('Helvetica', 12) )
acts_canvas = canvas1.create_window( 1000, 900, 
    anchor = "nw",
    window = acts)



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

canvas2 = tk.Canvas( Questions, width = 1920,height= 1200)

canvas2.pack(fill = "both", expand = True)


distL = tk.Label(Questions, text="What is the distance of this star from the earth?", font=('calibre',20,'normal'))
lumiL = tk.Label(Questions, text="What is the luminosity of this star?", font=('calibre',20,'normal'))
radiL = tk.Label(Questions, text="What is the radius of this star?", font=('calibre',20,'normal'))
tempL = tk.Label(Questions, text="What is the temperature of this star?",font=('calibre',20,'normal') )




distE = tk.Entry(Questions,textvariable = dist_var, font=('calibre',20,'normal'))
lumiE = tk.Entry(Questions,textvariable = lumi_var, font=('calibre',20,'normal'))
radiE = tk.Entry(Questions,textvariable = radi_var, font=('calibre',20,'normal'))
tempE = tk.Entry(Questions,textvariable = temp_var, font=('calibre',20,'normal'))





dist1_canvas = canvas2.create_window( 0, 0, anchor = "nw", window = distL)
lumi1_canvas = canvas2.create_window( 0, 100, anchor = "nw", window = lumiL)
radi1_canvas = canvas2.create_window( 0, 200, anchor = "nw", window = radiL)
temp1_canvas = canvas2.create_window( 0, 300, anchor = "nw", window = tempL)
dist2_canvas = canvas2.create_window( 0, 50, anchor = "nw", window = distE)
lumi2_canvas = canvas2.create_window( 0, 150, anchor = "nw", window = lumiE)
radi2_canvas = canvas2.create_window( 0, 250, anchor = "nw", window = radiE)
temp2_canvas = canvas2.create_window( 0, 350, anchor = "nw", window = tempE)



root.mainloop()