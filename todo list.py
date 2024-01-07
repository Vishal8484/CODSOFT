import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        completed_listbox.insert(tk.END, task)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_list():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear the entire to-do list?")
    if confirmed:
        listbox.delete(0, tk.END)
        completed_listbox.delete(0, tk.END)

#Create the window
root = tk.Tk()
root.title("Interactive To-Do List")

#Create pack widgets
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear List", command=clear_list)
clear_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=40)
completed_listbox.pack()

root.mainloop()
