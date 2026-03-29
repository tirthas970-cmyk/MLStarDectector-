import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os
import joblib

class MLStarDectector:
    def __init__(self):
        self.model = None
        self.file_name = 'TrainStarData.joblib'

    def TrainModel_Test(self, datalist):
        try:
            if not os.path.exists('star_dataset.csv'):
                return "Error: star_dataset.csv not found!"
            
            df = pd.read_csv('star_dataset.csv')
            # Adjust columns to match CSV
            X = df.drop(columns=['Name', 'Spectral Class'])
            y = df['Name']

            if os.path.exists(self.file_name):
                self.model = joblib.load(self.file_name)
            else:
                self.model = DecisionTreeClassifier()
                self.model.fit(X, y)
                joblib.dump(self.model, self.file_name)

            df_user_input = pd.DataFrame([datalist], columns=X.columns)
            star_names = self.model.classes_
            probs = self.model.predict_proba(df_user_input)
            best_index = np.argmax(probs)
            
            return f"Prediction: {star_names[best_index]}"
        except Exception as e:
            return f"Error: {str(e)}"

# Initialize the detector
detector = MLStarDectector()

# --- FRONTEND: MAIN WINDOW ---
root = tk.Tk()
root.title("Star-GPT")
root.geometry("800x600")

# Main Canvas
canvas1 = tk.Canvas(root, width=1920, height=1080, bg="#1a1a1a")
canvas1.pack(fill="both", expand=True)
bg = tk.PhotoImage(file="C:/Users/sukla/OneDrive/Pictures/Screenshots 1/Screenshot 2026-03-28 161338.png")
canvas1.create_image(0, 0, image = bg, anchor = "nw")

canvas1.create_text(775, 100, text="Star-GPT", fill="#FFBE46", font=("Helvetica", 50, "bold"))


choice = tk.StringVar()
choice.set("Select Action")
actions = ["Detect Star", "Get star info"]

# --- PREDICTION POPUP WINDOW ---
Questions = tk.Toplevel(root)
Questions.title("Enter Star Data")
Questions.geometry("400x550")
Questions.withdraw() # Keep hidden until needed

bg2 = tk.PhotoImage(file="C:/Users/sukla/OneDrive/Pictures/Screenshots 1/Screenshot 2026-03-28 155654.png")
canvas2 = tk.Canvas( Questions, width = 1920, height= 1200)
canvas2.create_image(0, 0, anchor = "nw")
# canvas2.pack(fill = "both", expand = True)

dist_var, lumi_var, radi_var, temp_var = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

def run_prediction():
    try:
        data = [
            float(dist_var.get()), 
            float(lumi_var.get()), 
            float(radi_var.get()), 
            float(temp_var.get())
        ]
        result = detector.TrainModel_Test(data)
        result_label.config(text=result, fg="#FFBE46")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter numbers only!")

input_frame = tk.Frame(Questions)
input_frame.pack(pady=20)

fields = [("Distance (ly):", dist_var), ("Luminosity (L/Lo):", lumi_var), 
          ("Radius (R/Ro):", radi_var), ("Temperature (K):", temp_var)]

for label_text, var in fields:
    tk.Label(input_frame, text=label_text, font=("Helvetica", 10)).pack()
    tk.Entry(input_frame, textvariable=var, justify='center').pack(pady=5)

predict_btn = tk.Button(input_frame, text="RUN ANALYSIS", command=run_prediction, 
                        bg="#FFBE46", width=20, font=("Helvetica", 10, "bold"))
predict_btn.pack(pady=20)

result_label = tk.Label(input_frame, text="Prediction: ---", font=("Helvetica", 12, "bold"))

result_label.pack()

# --- BUTTON LOGIC FOR MAIN SCREEN ---
def open_inputs():
    mode = choice.get()
    
    if mode == "Detect Star":
        Questions.deiconify() # Shows the data entry window
        
    elif mode == "Get star info":
        ask = simpledialog.askstring("Search", "What star do you want information on?")
        if ask:
            try:
                df = pd.read_csv('star_dataset.csv')
                star_info = df[df['Name'].str.lower() == ask.strip().lower()]
                if not star_info.empty:
                    # Formats the row into a readable string for the popup
                    details = star_info.iloc[0].to_string()
                    messagebox.showinfo(f"Info for {ask}", details)
                else:
                    messagebox.showerror("Not Found", f"Star '{ask}' not found.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read dataset: {e}")
    else:
        messagebox.showwarning("Selection Required", "Please select an action from the menu first!")

# --- ADDING BUTTONS TO MAIN SCREEN ---
acts = tk.OptionMenu(root, choice, *actions)
acts.config(width=20, font=("Helvetica", 12))
canvas1.create_window(950, 550, window=acts)

confirm_btn = tk.Button(root, text="Confirm Selection", command=open_inputs, 
                        width=20, height=2, bg="#FFBE46", font=("Helvetica", 12, "bold"))
canvas1.create_window(600, 550, window=confirm_btn)

root.mainloop()
