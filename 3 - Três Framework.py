import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

frame_first = tk.Frame(root, bg="lightblue")
frame_first.place (relx=0.1, rely=0.1, relwidth= 0.8,relheight=0.2)

frame_second = tk.Frame(root, bg="lightgreen")
frame_second.place (relx=0.1, rely=0.4, relwidth= 0.8,relheight=0.2)

frame_third = tk.Frame(root, bg="yellow")
frame_third.place (relx=0.1, rely=0.7, relwidth= 0.8,relheight=0.2)

label_first = tk.Label(frame_first, text="Primeiro Frame",font=("Roboto", 12), bg="lightblue")
label_first.place(relx= 0.5, rely= 0.4,anchor="center")

label_second = tk.Label(frame_second, text="Segundo Frame",font=("Roboto", 12), bg="lightgreen")
label_second.place(relx= 0.5, rely= 0.4,anchor="center")

label_third = tk.Label(frame_third, text="Terceiro Frame",font=("Roboto", 12), bg="yellow")
label_third.place(relx= 0.5, rely= 0.4,anchor="center")
root.mainloop()
