import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

frame_superior = tk.Frame(root, bg="lightblue")
frame_superior.place (relx=0.2, rely=0.8, relwidth= 0.8,relheight=0.2)

root.mainloop()
