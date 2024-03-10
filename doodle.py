from tkinter import *
from tkinter import ttk


def add_task():
    task_title = entered_task_title.get()
    print(f"Task Title: {task_title}")

root_main = Tk(className="Task Manager")

ttk.Label(root_main, text="Task Title: ").grid(column=0, row=0)
entered_task_title = Entry(root_main)
entered_task_title.grid(column=1, row=0)


ttk.Button(root_main, text="Add Task", command=add_task).grid(column=0, row=3)

root_main.mainloop()

