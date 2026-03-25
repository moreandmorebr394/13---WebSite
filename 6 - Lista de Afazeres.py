from tkinter import *
from tkinter import messagebox
tasks_list = []
counter = 1

def inputError():
    if enterTaskField.get() == "" :
        messagebox.showerror("Erro")

        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    value = inputError()
    if value == 0 :
        return
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + "]" + content)
    counter += 1
    clear_taskField()

def delete():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showerror("input error")
        return
    else:
        task_no = int (number)
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1

    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__" :
    gui = Tk()
    gui.configure(bg = "lightcoral")
    gui.title("Afazeres")
    gui.geometry("250x300")
    enterTask = Label(gui, text = "Adicionar Tarefa", bg="lavenderblush")

    enterTaskField = Entry(gui)

    Adicionar = Button(gui, text="Adicionar", fg = "Black", bg="darksalmon", command = insertTask)

    TextArea = Text(gui, height=5, width=25, font=("Roboto", 12 ))
    taskNumber = Label(gui, text = "Apague essa tarefa", bg="lavenderblush")
    taskNumberField = Text(gui, height = 1, width = 2, font =("Roboto", 12))
    delete = Button(gui, text="Apagar", fg = "Black", bg="indianred", command = delete)

    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    Adicionar.grid(row=2, column=2)

    TextArea.grid(row=3, column=2, padx=10, sticky= W)
    taskNumber.grid(row=4, column=2, pady=5)

    delete.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=2)

    gui.mainloop()
    
