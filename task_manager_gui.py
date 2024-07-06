import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task_title = entry_task_title.get()
    description = entry_description.get()
    priority = priority_var.get()
    category = category_var.get()

    if task_title and priority:
        task_info = (task_title, priority, "Incomplete", category, description)
        tree.insert("", tk.END, values=task_info)
        entry_task_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        priority_var.set("Low")
        category_var.set("General")
    else:
        messagebox.showwarning("Task Manager", "Please enter a task title and select a priority.")

def delete_task():
    selected_task_index = tree.selection()
    if selected_task_index:
        tree.delete(selected_task_index)
    else:
        messagebox.showwarning("Task Manager", "Please select a task to delete.")

def toggle_status(event):
    item = tree.focus()
    if item and tree.identify_column(event.x) == '#3':  # Only toggle status if the status column is clicked
        current_status = tree.item(item, 'values')[2]
        new_status = "Complete" if current_status == "Incomplete" else "Incomplete"
        values = list(tree.item(item, 'values'))
        values[2] = new_status
        tree.item(item, values=values)

def show_description(event):
    item = tree.focus()
    if item and tree.identify_column(event.x) == '#1':  # Only show description if the task title column is double-clicked
        description = tree.item(item, 'values')[4]
        messagebox.showinfo("Task Description", f"Description:\n\n{description}")

# Create the main application window
root = tk.Tk()
root.title("Task Manager")

# Create and place widgets
label_task_title = tk.Label(root, text="Task Title:")
label_task_title.grid(row=0, column=0, padx=10, pady=10)

entry_task_title = tk.Entry(root)
entry_task_title.grid(row=0, column=1, padx=10, pady=10)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=1, column=0, padx=10, pady=10)

entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1, padx=10, pady=10)

label_priority = tk.Label(root, text="Priority:")
label_priority.grid(row=0, column=2, padx=10, pady=10)

# Priority dropdown menu
priority_var = tk.StringVar(root)
priority_var.set("Low")
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=0, column=3, padx=10, pady=10)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=0, column=4, padx=10, pady=10)

# Category dropdown menu
category_var = tk.StringVar(root)
category_var.set("General")
category_menu = tk.OptionMenu(root, category_var, "General", "Work", "Personal", "Other")
category_menu.grid(row=0, column=5, padx=10, pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=6, padx=10, pady=10)

# Task Table (Treeview)
columns = ("Task Title", "Priority", "Status", "Category")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=2, column=0, columnspan=7, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.grid(row=3, column=0, columnspan=7, pady=10)

# Bind the toggle_status function to mouse click on the status column
tree.bind("<Button-1>", toggle_status)

# Bind the show_description function to double-click on the task title
tree.bind("<Double-1>", show_description)

# Start the Tkinter event loop
root.mainloop()
