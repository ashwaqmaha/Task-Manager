import argparse
import sys
import csv
import random
from tabulate import tabulate

def validate_priority(priority):
    valid_priorities = ["low", "medium", "high"]
    if priority.lower() in valid_priorities:
        return True
    else:
        print(f"Invalid priority '{priority}'. Please enter one of the following: {', '.join(valid_priorities)}")
        return False
    
def validate_non_empty(value, field_name):
    if value.strip():
        return True
    else:
        print(f"{field_name} cannot be empty. Please enter a valid {field_name.lower()}.")
        return False

def save_data(task_id, task_title, task_description, priority, category):
    with open("tasks_info.csv", "a", newline='') as file:
        data_writer = csv.writer(file)
        data_writer.writerow([task_id, task_title, task_description, priority, category, "Incomplete"])
    print("Task successfully added!")

def mark_complete(task_id):
    tasks = []
    task_found = False
    with open("tasks_info.csv", "r", newline='') as file:
        data_reader = csv.reader(file)
        for row in data_reader:
            if row[0] == task_id:
                row[5] = "Complete"
                task_found = True
            tasks.append(row)

    if task_found:
        with open("tasks_info.csv", "w", newline='') as file:
            data_writer = csv.writer(file)
            data_writer.writerows(tasks)
        print(f"Task {task_id} marked as complete!")
    else:
        print(f"Task with ID {task_id} not found!")

def delete_task(task_id):
    tasks = []
    task_found = False
    with open("tasks_info.csv", "r", newline='') as file:
        data_reader = csv.reader(file)
        for row in data_reader:
            if row[0] == task_id:
                task_found = True
            else:
                tasks.append(row)

    if task_found:
        with open("tasks_info.csv", "w", newline='') as file:
            data_writer = csv.writer(file)
            data_writer.writerows(tasks)
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task with ID {task_id} not found!")

def view_task_details(task_id):
    with open("tasks_info.csv", "r", newline='') as file:
        data_reader = csv.reader(file)
        for row in data_reader:
            if row[0] == task_id:
                print(f"Title: {row[1]}")
                print(f"Description:\n{row[2]}")
                return
    print(f"Task with ID {task_id} not found!")

def unique_ids():
    id_list = []
    with open("tasks_info.csv", "r", newline='') as files:
        data_reader = csv.reader(files)
        for line in data_reader:
            id_list.append(line[0])
    return id_list

def create_unique_id():
    id_list = unique_ids()
    while True:
        i = random.randrange(0, 1000)
        if len(id_list) == 0:
            return i
        elif not str(i) in id_list:
            return i

def remove_unique_id(id):
    id_collection = set(unique_ids())
    id_collection.discard(id)


def add_task():
    while True:
        task_title = input("Enter Task Title: ")
        if validate_non_empty(task_title, "Task Title"):
            break
    task_description = input("Enter description: ")
    while True:
        priority = input("Enter Priority level (low/medium/high): ")
        if validate_priority(priority):
            break
    while True:
        category = input("Enter Category (General/personal/work/other): ")
        if validate_non_empty(category, "Category"):
            break
    task_id = create_unique_id()
    save_data(task_id, task_title, task_description, priority, category)

def display_tasks():
    all_data = [["Task id", "Task title", "Priority", "Category", "Status"]]
    with open("tasks_info.csv", "r", newline='') as files:
        data_reader = csv.reader(files)
        for line in data_reader:
            if len(line) > 0:
                display = [line[0], line[1], line[3], line[4], line[5]]
                all_data.append(display)
    if len(all_data) > 1:
        return tabulate(all_data, headers="firstrow", tablefmt="fancy_grid")
    else:
        return "Currently no tasks!"

def complete_task():
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id of the task to mark as complete: ")
        mark_complete(task_id)

def delete_task_prompt():
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id of the task to delete: ")
        delete_task(task_id)

def view_task_prompt():
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id to view details: ")
        view_task_details(task_id)

def instructions(version):
    print(f"""
Terminal Task Manager
          
In the fast-paced world we live in, staying organised 
and on top of your tasks is essential for success. 
Introducing Terminal Task Manager, your ultimate 
companion in conquering the chaos of daily life for developers. 
          
Usage Instructions:
          
Command-Line interface: 
          
use the following command: python{version} task_manager.py [option]

Graphical User interface: 

use the following command: python{version} task_manager_gui.py 

options:
  -h, --help                Show help message and exit
  --add                     Add a new task
  --display                 Display tasks
  --complete                Mark a task as completed
  --delete                  Delete a task
  --view                    View task details
""")

def main():
    version = sys.version_info.major

    parser = argparse.ArgumentParser(description="Command-Line Task Manager")
    parser.add_argument("--add", help="Add a new task", action="store_true")
    parser.add_argument("--display", help="Display tasks", action="store_true")
    parser.add_argument("--complete", help="Mark a task as completed", action="store_true")
    parser.add_argument("--delete", help="Delete a task", action="store_true")
    parser.add_argument("--view", help="View task details", action="store_true")

    args = parser.parse_args()

    if args.add:
        add_task()
    elif args.display:
        display = display_tasks()
        print(display)
    elif args.complete:
        complete_task()
    elif args.delete:
        delete_task_prompt()
    elif args.view:
        view_task_prompt()
    else:
        instructions(version)

if __name__ == "__main__":
    main()
