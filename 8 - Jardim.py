import tkinter as tk


app = tk.Tk()
app.title("Jardim")
app.geometry("700x600")

frame_pagina = tk.Frame(app, bg="lightblue")
frame_pagina.place (relx=0, rely= 0,relwidth= 10,relheight=0.4)

frame_ceu_um = tk.Frame(app, bg="white")
frame_ceu_um.place (relx= 0.1, rely= 0.05, relwidth= 0.2, relheight= 0.2)

frame_ceu_dois = tk.Frame(app, bg="white")
frame_ceu_dois.place (relx= 0.7, rely= 0.03, relwidth= 0.2, relheight= 0.2)

mato = tk.Frame(app, bg="lightgreen")
mato.place (relx= 0, rely=0.4, relwidth=10, relheight=10)

flor_um = tk.Frame(app, bg="lightpink")
flor_um.place (relx= 0.2, rely=0.5, relwidth=0.1, relheight=0.1, anchor="center")

flor_um_centro = tk.Frame(app, bg="palevioletred")
flor_um_centro.place (relx= 0.2, rely=0.5, relwidth=0.05, relheight=0.05)

cabo = tk.Frame(app, bg="forest green")
cabo.place (relx= 0.2, rely=0.6, relwidth=0.02, relheight=0.2, anchor="nw")

app.mainloop()
