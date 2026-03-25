import tkinter as tk


app = tk.Tk()
app.title("Jardim")
app.geometry("700x600")

frame_pagina = tk.Frame(app, bg="lightblue")
frame_pagina.place (relx=0, rely= 0,relwidth= 10,relheight=0.4)

frame_ceu_um = tk.Frame(app, bg="white")
frame_ceu_um.place (relx= 0.1, rely= 0.05, relwidth= 0.2, relheight= 0.1)

frame_ceu_dois = tk.Frame(app, bg="white")
frame_ceu_dois.place (relx= 0.7, rely= 0.03, relwidth= 0.2, relheight= 0.2)

mato = tk.Frame(app, bg="lightgreen")
mato.place (relx= 0, rely=0.4, relwidth=10, relheight=10)

cabo_um = tk.Frame(app, bg="forest green")
cabo_um.place (relx= 0.2, rely=0.5, relwidth=0.02, relheight=0.2, anchor="nw")
flor_um = tk.Frame(app, bg="lightpink")
flor_um.place (relx= 0.2, rely=0.5, relwidth=0.1, relheight=0.1, anchor="center")
flor_um_centro = tk.Frame(app, bg="palevioletred")
flor_um_centro.place (relx= 0.2, rely=0.5, relwidth=0.04, relheight=0.04)

cabo_dois = tk.Frame(app, bg="forest green")
cabo_dois.place (relx= 0.3, rely=0.7, relwidth=0.02, relheight=0.2, anchor="nw")
flor_dois = tk.Frame(app, bg="medium orchid")
flor_dois.place (relx= 0.3, rely=0.7, relwidth=0.1, relheight=0.1, anchor="center")
flor_dois_centro = tk.Frame(app, bg="medium purple")
flor_dois_centro.place (relx= 0.3, rely=0.7, relwidth=0.04, relheight=0.04)

cabo_tres = tk.Frame(app, bg="forest green")
cabo_tres.place (relx= 0.5, rely=0.5, relwidth=0.02, relheight=0.2, anchor="nw")
flor_tres = tk.Frame(app, bg="dark salmon")
flor_tres.place (relx= 0.5, rely=0.5, relwidth=0.1, relheight=0.1, anchor="center")
flor_tres_centro = tk.Frame(app, bg="dark orange")
flor_tres_centro.place (relx= 0.5, rely=0.5, relwidth=0.04, relheight=0.04)

cabo_quatro = tk.Frame(app, bg="forest green")
cabo_quatro.place (relx= 0.4, rely=0.3, relwidth=0.02, relheight=0.2, anchor="nw")
flor_quatro = tk.Frame(app, bg="turquoise1")
flor_quatro.place (relx= 0.4, rely=0.3, relwidth=0.1, relheight=0.1, anchor="center")
flor_quatro_centro = tk.Frame(app, bg="light cyan")
flor_quatro_centro.place (relx= 0.4, rely=0.3, relwidth=0.04, relheight=0.04)

app.mainloop()
