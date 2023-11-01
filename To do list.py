import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create task entry
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT)

# Create task listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

# Start the main loop
root.mainloop()
