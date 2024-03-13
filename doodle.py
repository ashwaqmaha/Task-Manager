# import tkinter as tk
# from tkinter import ttk, messagebox

# def add_task():
#     task_title = entry_task_title.get()
#     priority = priority_var.get()

#     if task_title and priority:
#         task_info = (task_title, priority, "Incomplete")
#         tree.insert("", tk.END, values=task_info)
#         entry_task_title.delete(0, tk.END)  # Clear the entry widget
#         priority_var.set("Low")  # Reset priority to default
#     else:
#         messagebox.showwarning("Task Manager", "Please enter a task title and select a priority.")

# def delete_task():
#     selected_task_index = tree.selection()
#     if selected_task_index:
#         tree.delete(selected_task_index)
#     else:
#         messagebox.showwarning("Task Manager", "Please select a task to delete.")

# def toggle_status(event):
#     item = tree.focus()
#     if item:
#         current_status = tree.item(item, 'values')[-1]
#         new_status = "Complete" if current_status == "Incomplete" else "Incomplete"
#         tree.item(item, values=(tree.item(item, 'values')[0], tree.item(item, 'values')[1], new_status))

# # Create the main application window
# root = tk.Tk()
# root.title("Task Manager")

# # Create and place widgets
# label_task_title = tk.Label(root, text="Task Title:")
# label_task_title.grid(row=0, column=0, padx=10, pady=10)

# entry_task_title = tk.Entry(root)
# entry_task_title.grid(row=0, column=1, padx=10, pady=10)

# label_priority = tk.Label(root, text="Priority:")
# label_priority.grid(row=0, column=2, padx=10, pady=10)

# # Priority dropdown menu
# priority_var = tk.StringVar(root)
# priority_var.set("Low")  # Default priority
# priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
# priority_menu.grid(row=0, column=3, padx=10, pady=10)

# button_add_task = tk.Button(root, text="Add Task", command=add_task)
# button_add_task.grid(row=0, column=4, padx=10, pady=10)

# # Task Table (Treeview)
# columns = ("Task Title", "Priority", "Status")
# tree = ttk.Treeview(root, columns=columns, show="headings")

# for col in columns:
#     tree.heading(col, text=col)
#     tree.column(col, width=150)

# tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

# button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
# button_delete_task.grid(row=2, column=0, columnspan=5, pady=10)

# # Bind the toggle_status function to mouse click on the status column
# tree.bind("<Button-1>", toggle_status)

# # Start the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task_title = entry_task_title.get()
    priority = priority_var.get()
    category = category_var.get()

    if task_title and priority:
        task_info = (task_title, priority, "Incomplete", category)
        tree.insert("", tk.END, values=task_info)
        entry_task_title.delete(0, tk.END)  # Clear the entry widget
        priority_var.set("Low")  # Reset priority to default
        category_var.set("General")  # Reset category to default
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
    if item:
        current_status = tree.item(item, 'values')[-2]
        new_status = "Complete" if current_status == "Incomplete" else "Incomplete"
        tree.item(item, values=(tree.item(item, 'values')[0], tree.item(item, 'values')[1], new_status, tree.item(item, 'values')[3]))

# Create the main application window
root = tk.Tk()
root.title("Task Manager")

# Create and place widgets
label_task_title = tk.Label(root, text="Task Title:")
label_task_title.grid(row=0, column=0, padx=10, pady=10)

entry_task_title = tk.Entry(root)
entry_task_title.grid(row=0, column=1, padx=10, pady=10)

label_priority = tk.Label(root, text="Priority:")
label_priority.grid(row=0, column=2, padx=10, pady=10)

# Priority dropdown menu
priority_var = tk.StringVar(root)
priority_var.set("Low")  # Default priority
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=0, column=3, padx=10, pady=10)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=0, column=4, padx=10, pady=10)

# Category dropdown menu
category_var = tk.StringVar(root)
category_var.set("General")  # Default category
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

tree.grid(row=1, column=0, columnspan=7, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.grid(row=2, column=0, columnspan=7, pady=10)

# Bind the toggle_status function to mouse click on the status column
tree.bind("<Button-1>", toggle_status)

# Start the Tkinter event loop
root.mainloop()
