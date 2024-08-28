import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the list
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks from the list
def clear_all_tasks():
    task_listbox.delete(0, tk.END)

# Function to display the number of tasks
def number_tasks():
    total_tasks = task_listbox.size()
    messagebox.showinfo("Number of Tasks", f"Total tasks: {total_tasks}")

# Function to update the selected task
def update_task():
    try:
        task_index = task_listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(task_index)
            task_listbox.insert(task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task to update.")
    except:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("800x600")
root.configure(bg="#d0e8f2")

# Entry widget for adding tasks
task_entry = tk.Entry(root, font=("Helvetica", 16), width=35)
task_entry.pack(pady=20)

# Submit button to add tasks
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 16), bg="#5aa897", fg="white", command=add_task)
submit_button.pack(pady=10)

# Frame to hold the listbox and scrollbar
list_frame = tk.Frame(root, bg="#d0e8f2")
list_frame.pack(pady=20)

# Listbox to display tasks
task_listbox = tk.Listbox(list_frame, width=40, height=10, font=("Helvetica", 16))
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Frame for the buttons
button_frame = tk.Frame(root, bg="#d0e8f2")
button_frame.pack(pady=20)

# Buttons for task operations
delete_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 14), bg="#f76c6c", fg="white", command=delete_task)
delete_button.grid(row=0, column=0, padx=10, pady=10)

clear_button = tk.Button(button_frame, text="Delete All", font=("Helvetica", 14), bg="#f76c6c", fg="white", command=clear_all_tasks)
clear_button.grid(row=0, column=1, padx=10, pady=10)

number_button = tk.Button(button_frame, text="Number of Tasks", font=("Helvetica", 14), bg="#4cbbb9", fg="white", command=number_tasks)
number_button.grid(row=1, column=0, padx=10, pady=10)

update_button = tk.Button(button_frame, text="Update Task", font=("Helvetica", 14), bg="#4cbbb9", fg="white", command=update_task)
update_button.grid(row=1, column=1, padx=10, pady=10)

# Exit button to close the application
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14), bg="#f76c6c", fg="white", command=root.quit)
exit_button.pack(pady=20)

# Run the main event loop
root.mainloop()
