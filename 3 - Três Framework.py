
import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

frame_inferior_direito = tk.Frame(root, height=700, width=1400, bg="yellow")
frame_inferior_direito.place (relx=0, rely=0, relwidth= 50,relheight=100)
#frame_inferior_direito.pack(fill=tk.Y, side=tk.RIGHT)
label_inferior_direito = tk.Label(frame_inferior_direito, text="Frame Inferior Direito", bg="yellow")
label_inferior_direito.place(anchor="se")


frame_direito = tk.Frame(root, height=500, width=1400, bg="lightgreen")
frame_direito.place (relx=0, rely=0,relwidth= 200,relheight=0.70)
#frame_direito.pack(fill=tk.X, side=tk.BOTTOM)
label_direito = tk.Label(frame_direito, text="Frame Direito",font=("Roboto", 12), bg="lightgreen")
label_direito.place(anchor="e")

frame_esquerdo = tk.Frame(root, height=700, width=200, bg="lightblue")
frame_esquerdo.place (relx=0, rely=0, relwidth= 0.2,relheight=100)
#frame_esquerdo.pack(side=tk.TOP)
label_esquerdo = tk.Label(frame_esquerdo, text="Frame Esquerdo", bg="lightblue")
label_esquerdo.place(anchor="nw")


root.mainloop()
