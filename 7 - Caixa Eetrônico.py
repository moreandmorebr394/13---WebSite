import tkinter as tk
from tkinter import messagebox

class CaixaEletronico:
    def __init__(self, root):
        self.root = root
        self.root.title("Caixa Eletrônico")
        self.saldo = 1000.00 # Saldo inicial

        self.label_saldo = tk.Label(root, text=f"Caixa Eletrônico", font=("Roboto", 16), bg="indianred")
        self.label_saldo.pack(pady=20)

        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack()

        self.btn_sacar = tk.Button(root, text="Sacar", command=self.sacar)
        self.btn_sacar.pack(pady=5)

    def sacar(self):
        try:
            valor = float(self.entry_valor.get())
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                self.atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
            else:
                messagebox.showwarning("Erro", "Saldo insuficiente ou valor inválido")
        except ValueError:
            messagebox.showerror("Erro", "Insira um número válido")

root = tk.Tk()
app = CaixaEletronico(root)
root.geometry("600x200")
root.mainloop()
