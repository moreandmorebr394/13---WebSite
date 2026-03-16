import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

frame_esquerdo = tk.Frame(root, height=700, width=1400, bg="yellow")
frame_esquerdo.place (relx=0, rely=0)

label_esquerdo = tk.Label(frame_esquerdo, text="Frame Inferior Esquerdo", bg="yellow")
label_esquerdo.place(relx=0.75, rely=0.75)

frame_direito = tk.Frame(root, height=500, width=1400, bg="lightgreen")
frame_direito.place (relx=0, rely=0)

label_direito = tk.Label(frame_direito, text="Frame Direito", bg="light green")
label_direito.place(relx=0.25, rely=0.25)

frame_inferior_direito = tk.Frame(root, height=700, width=200, bg="lightblue")
frame_inferior_direito.place (relx=0, rely=0)

label_inferior_direito = tk.Label(frame_esquerdo, text="Frame Esquerdo", bg="lightblue")
label_inferior_direito.place(relx=0, rely=0.50)

root.mainloop()
