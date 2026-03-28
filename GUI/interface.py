import tkinter as tk 







root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
root.geometry("1920x1080")
bg = tk.PhotoImage(file="C:/Users/peach/Downloads/pexels-felix-mittermeier-956981.png")

# Create Canvas
canvas1 = tk.Canvas( root, width = 1920,
                 height = 1200)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")



def btn_click(): 
    buttonA["state"] = "enabled"

buttonA = tk.Button(root, text="idk yet", height=5, width=20, activebackground="#ff0000")
buttonA_canvas = canvas1.create_window( 300, 300, 
    anchor = "nw",
    window = buttonA)


root.mainloop()