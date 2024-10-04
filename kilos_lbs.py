import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x320")
root.title("Pounds/Kilos")

title_label = tk.Label(root, 
                      text="Pounds / Kilos",
                      padx=100,
                      pady=13,
                      font=('Arial', 27),
                      background="midnightblue",
                      foreground="white")
title_label.pack()

# Labels for "amount", "from", and "to"
amount_label = tk.Label(root, text="AMOUNT:", font=("Arial", 13))
amount_label.place(x=20, y=80)

from_label = tk.Label(root, text="FROM:", font=("Arial", 13))
from_label.place(x=20, y=110)

to_label = tk.Label(root, text="TO:", font=("Arial", 13))
to_label.place(x=20, y=140)

# Entry and dropdown widgets
amount_entry = tk.Entry(root, width=23)
amount_entry.place(x=110, y=84)

from_dropdown = ttk.Combobox(state="readonly", values=["Pound", "Kilo"])
from_dropdown.place(x=110, y=114)

to_dropdown = ttk.Combobox(state="readonly", values=["Pound", "Kilo"])
to_dropdown.place(x=110, y=144)

# Label for displaying results or errors
result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.place(x=20, y=220)

def is_number(s):
    try:
        float(s)  # Try converting to float
        return True
    except ValueError:
        return False

def getter():
    amount_text = amount_entry.get()
    
    if is_number(amount_text):
        amount = float(amount_text)
        from_unit = from_dropdown.get()
        to_unit = to_dropdown.get()
        return amount, from_unit, to_unit
    else:
        return None, None, None

def cal():
    amount, from_unit, to_unit = getter()

    if amount is None:
        return "Invalid input or no Input"

    if amount > 0 and from_unit == "Kilo" and to_unit == "Pound":
        return amount * 2.20462
    
    elif amount > 0 and from_unit == "Pound" and to_unit == "Kilo":
        return amount / 2.20462
    
    elif amount > 0 and from_unit == to_unit:
        return "Units of measurement should\nnot match each other!"
    
    elif amount <= 0:
        return "Amount must be more than zero"
    
    else:
        return "IDK"

def printer():
    result = cal()
    amount, from_unit, to_unit = getter()
    
    # Clear the previous text
    result_label.config(text="")

    # Check if result is a number before formatting
    if isinstance(result, (int, float)):
        result_label.config(text=f"{amount} {from_unit} into {to_unit} = {result:.2f}")
    else:
        result_label.config(text=result)

button = tk.Button(root, 
                   text="CONVERT",
                   padx=15,
                   pady=2,
                   bg="midnightblue",
                   foreground="white",
                   font=("Arial", 13),
                   command=printer)  
button.place(x=80, y=175)

root.mainloop()
