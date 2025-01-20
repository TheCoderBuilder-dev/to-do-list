import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, task + " (Done)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Create widgets
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=20)

add_button = tk.Button(root, text="Add Task", width=20, font=("Arial", 14), command=add_task)
add_button.pack(pady=10)

tasks_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 14), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", width=20, font=("Arial", 14), command=delete_task)
delete_button.pack(pady=10)

mark_done_button = tk.Button(root, text="Mark as Done", width=20, font=("Arial", 14), command=mark_done)
mark_done_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
