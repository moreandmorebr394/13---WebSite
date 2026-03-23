import tkinter as tk

from tkinter import *  # Import all components from tkinter
from tkinter import messagebox

# Create the main window (Master Window B)
B = tk.Tk()
B.title("Countdown Timer")

# Set window size
B.geometry("300x200")

# Time variable
time_left = 0

# Timer label
timer_label = Label(B, text="00", font=("Roboto", 48), bg="lavenderblush")
timer_label.pack()

# Time input entry
time_input = Entry(B, font=("Roboto", 14), bg="mintcream")
time_input.pack(pady=10)

# Helper functions
def start_timer():
    global time_left
    try:
        time_left = int(time_input.get()) * 60  # Convert minutes to seconds
        countdown()
    except ValueError:
        messagebox.showerror("Entrada Inválida", "Coloque um Número Válido.")

def countdown():
    global time_left
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{secs:02d}")
        time_left -= 1
        B.after(1000, countdown)  # Update every second
    else:
        messagebox.showinfo("Time's Up!", "Tempo acabou.")

def reset_timer():
    global time_left
    time_left = 0
    timer_label.config(text="00")
    time_input.delete(0, END)

# Buttons
start_button = Button(B, text="Start", font=("Roboto", 14), bg = "lavenderblush", command=start_timer)
start_button.pack(side="left", padx=20)

reset_button = Button(B, text="Reset", font=("Roboto", 14),bg = "lavenderblush", command=reset_timer)
reset_button.pack(side="right", padx=20)

B.mainloop()
