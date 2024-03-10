import tkinter as tk
from tkinter import messagebox

def add_task():
    task_title = entry_task_title.get()
    if task_title:
        listbox_tasks.insert(tk.END, task_title)
        entry_task_title.delete(0, tk.END)  # Clear the entry widget
    else:
        messagebox.showwarning("Task Manager", "Please enter a task title.")


# Create the main application window
root = tk.Tk()
root.title("Task Manager")

# Create and place widgets
label_task_title = tk.Label(root, text="Task Title:")
label_task_title.grid(row=0, column=0, padx=10, pady=10)

entry_task_title = tk.Entry(root)
entry_task_title.grid(row=0, column=1, padx=10, pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=2, padx=10, pady=10)

listbox_tasks = tk.Listbox(root)
listbox_tasks.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)



# Start the Tkinter event loop
root.mainloop()


