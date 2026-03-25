import tkinter as tk
from tkinter import messagebox

def realizar_saque():
    try:
        valor = int(entry_valor.get())
        if valor <= 0:
            messagebox.showwarning("Erro", "Insira um valor maior")
            return
        
        notas = [100, 50, 20, 10, 5, 2]
        resultado = []

        valor_restante = valor
        for nota in notas:
            qtd = valor_restante // nota
            valor_restante %= nota
            if qtd > 0:
                resultado.append(f"{qtd} notas(s) de R$ {nota}")

        if valor_restante > 0:
            messagebox.showinfo("Dinheiro Sacado")
        
        else:
            messagebox.showinfo("Saque", f"Saque realizado:\n" + "\n".join(resultado))
            
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros.")

app = tk.Tk()
app.title("Caixa Eletrônico")
app.geometry("400x300")

frame_pagina = tk.Frame(app, bg="lavenderblush")
frame_pagina.place (relwidth= 10,relheight=10)

label_instrucao = tk.Label(app, text="Caixa Eletrônico", font=("Roboto", 16), bg="lavenderblush")
label_instrucao.pack(pady=10)

entry_valor = tk.Entry(app, font=("Roboto", 10), bg="lavender")
entry_valor.pack(pady=5)

btn_sacar = tk.Button(app, text="Sacar", command= realizar_saque, bg="hotpink", font=("Roboto", 12))
btn_sacar.pack(pady=15)

app.mainloop()
