import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    if name and age and email:
        messagebox.showinfo("Registration Info", f"Name: {name}\nAge: {age}\nEmail: {email}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# Create the main window
root = tk.Tk()
root.title("Simple Registration Form")
root.geometry("300x200")

# Create and place the labels and entry widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the submit button
tk.Button(root, text="Submit", command=submit).grid(row=3, column=1, pady=10)

# Run the main loop
root.mainloop()
