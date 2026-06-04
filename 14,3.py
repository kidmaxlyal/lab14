import tkinter as tk

class IceCreamStand:
    def __init__(self):
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное","фисташковое"]

cafe = IceCreamStand()
window = tk.Tk()
window.title("Кафе-мороженое siuuu")

listbox = tk.Listbox(window)
for f in cafe.flavors:
    listbox.insert(tk.END, f)
listbox.pack()

entry = tk.Entry(window)
entry.pack()

def add():
    cafe.flavors.append(entry.get())
    listbox.insert(tk.END, entry.get())
tk.Button(window, text="Добавить", command=add).pack()

def remove():
    sel = listbox.curselection()
    if sel:
        cafe.flavors.pop(sel[0])
        listbox.delete(sel[0])
tk.Button(window, text="Удалить", command=remove).pack()

window.mainloop()