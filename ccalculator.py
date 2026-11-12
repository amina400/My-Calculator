
import tkinter as tk

def click(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def back():
    entry.delete(len(entry.get())-1, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "ভুল!")

window = tk.Tk()
window.title("আমার ক্যালকুলেটর")
window.geometry("320x480")
window.configure(bg="#1e1e2e")

entry = tk.Entry(window, font=("Arial", 28),
                  justify="right", bg="#2a2a3d", fg="white", borderwidth=0)
entry.pack(fill="x", padx=15, pady=20, ipady=15)

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["(", "0", ")", "."],
]

for row in buttons:
    frame = tk.Frame(window, 
                     bg="#1e1e2e")
    frame.pack()
    for btn in row:
        if btn == "C":
            color = "#ff5555"
            cmd = clear
        elif btn == "⌫":
            color = "#ffaa00"
            cmd = back
        elif btn in ["%", "/", "*", "-", "+"]:
            color = "#ffaa00"
            cmd = lambda v=btn: click(v)
        elif btn in ["(", ")"]:
            color = "#00ccff"
            cmd = lambda v=btn: click(v)
        else:
            color = "#3a3a55"
            cmd = lambda v=btn: click(v)

        b = tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 16, "bold"), bg=color, fg="white", borderwidth=0, command=cmd)
        b.pack(side="left", padx=4, pady=4)

eq = tk.Button(window, text="=", width=22, height=2, font=("Arial", 18, "bold"), bg="#00cc66", fg="white", borderwidth=0, command=equal)
eq.pack(pady=8)

window.mainloop()