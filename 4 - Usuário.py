import tkinter as tk

root = tk.Tk()
root.geometry("1400x700")
root.title("Estrutura Base")

name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=passw_var.get()

    print("O nome é: " + name)
    print("A senha é: " + password)

    name_var.set("")
    passw_var.set("")
#Tela inicial do login

frame_pagina = tk.Frame(root, bg="maroon")
frame_pagina.place (relx=0.1, rely=0.10, relwidth= 0.8,relheight=0.40)

#Nome usado na entrada
name_label = tk.Label(frame_pagina, text='Digite seu email:', font=('Roboto', 12), bg="indianred")
name_label.place(relx=0.1, rely=0.10)

name_entry = tk.Entry(frame_pagina, textvariable= name_var, font=('Roboto', 12), show="*")
name_entry.place(relx= 0.22, rely=0.10)

passw_label = tk.Label(frame_pagina, text='Digite sua senha:', font=('Roboto', 12), bg="indianred")
passw_label.place(relx=0.1, rely=0.25)

passw_entry = tk.Entry(frame_pagina, textvariable= passw_var, font=('Roboto', 12))
passw_entry.place(relx= 0.22, rely=0.25)

sub_btn=tk.Button(frame_pagina, text='Enviar', command = submit, bg="indianred")
sub_btn.place(relx= 0.29, rely=0.35, anchor="center")

name_label.grid(row=8,column=9)
name_entry.grid(row=11,column=10)
passw_label.grid(row=11,column=9)
passw_entry.grid(row=8,column=10)
sub_btn.grid(row=13,column=10)
#Local do email e senha

frame_second = tk.Frame(root, bg="maroon")
frame_second.place (relx=0.1, rely=0.55, relwidth= 0.8,relheight=0.35)

label_second = tk.Label(frame_second, text="Email: b3a@gmail.com",font=("Roboto", 12), bg="maroon")
label_second.place(relx= 0.5, rely= 0.4,anchor="center")

label_second = tk.Label(frame_second, text="Senha: 758496",font=("Roboto", 12), bg="maroon")
label_second.place(relx= 0.5, rely= 0.5,anchor="center")

#frame_pagina = tk.Frame(root, bg="tomato")
#frame_pagina.place (relx=0.1, rely=0, relwidth= 0.8,relheight=0.05)


root.mainloop()
