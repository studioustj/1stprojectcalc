import tkinter as tk

def on_click(char):
    #Only button clicks will be processed
    current = entry.get()
    if char == "=":
        try:
            expression = current.replace('·', '*')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=('Times New Roman', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4, padx=4, pady=5)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('·', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2,
                       command=lambda char=text: on_click(char))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

root.mainloop()