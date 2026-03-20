import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

#Telas com cores diversas de proporções diferentes

frame_pagina = tk.Frame(root, bg="tomato")
frame_pagina.place (relx=0.1, rely=0, relwidth= 0.8,relheight=0.05)

frame_first = tk.Frame(root, bg="lightsalmon")
frame_first.place (relx=0.1, rely=0.11, relwidth= 0.8,relheight=0.2)

frame_second = tk.Frame(root, bg="maroon")
frame_second.place (relx=0.1, rely=0.32, relwidth= 0.8,relheight=0.4)

frame_third = tk.Frame(root, bg="palevioletred")
frame_third.place (relx=0.1, rely=0.73, relwidth= 0.8,relheight=0.2)

#Nome de cada tela

label_pagina = tk.Label(frame_pagina, text="Páginas de Código",font=("Impact", 12), bg="tomato")
label_pagina.place(relx= 0.5, rely= 0.4,anchor="center")

label_first = tk.Label(frame_first, text="Primeiro Frame",font=("Roboto", 12), bg="lightsalmon")
label_first.place(relx= 0.5, rely= 0.4,anchor="center")

label_second = tk.Label(frame_second, text="Segundo Frame",font=("Roboto", 12), bg="maroon")
label_second.place(relx= 0.5, rely= 0.4,anchor="center")

label_third = tk.Label(frame_third, text="Terceiro Frame",font=("Roboto", 12), bg="palevioletred")
label_third.place(relx= 0.5, rely= 0.4,anchor="center")
root.mainloop()
