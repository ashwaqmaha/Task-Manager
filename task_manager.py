import argparse
import sys
import csv
import random
from tabulate import tabulate

def validate_priority(priority):
    """Validate the priority level."""
    vaild_priorities = ["low", "medium", "high"]
    if priority.lower() in vaild_priorities:
        return True
    print(f"Invalid priority '{priority}'. Please enter one of the following: {', '.join(vaild_priorities)}")
    return False
    
def validate_non_empty(value, field_name):
    """Validate that a field is not empty."""
    if value.strip():
        return True
    print(f"{field_name} cannot be empty. Please enter a valid {field_name.lower()}.")
    return False

def save_data(task_id, task_title, task_description, priority, category):
    """Save task data to the CSV file."""
    try:
        with open("tasks_info.csv", "a", newline='') as file:
            data_writer = csv.writer(file)
            data_writer.writerow([task_id, task_title, task_description, priority, category, "Incomplete"])
        print("Task successfully added!")
    except IOError as e:
        print("An error occurred while saving the task. Please try again.")
        

def mark_complete(task_id):
    """Mark a task as complete."""
    tasks = []
    task_found = False
    try:
        with open("tasks_info.csv", "r", newline='') as file:
            data_reader = csv.reader(file)
            for row in data_reader:
                if len(row) > 0:
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
            print(f"Task with ID {task_id} not found. Please check the ID and try again.")
            
    except IOError as e:
        print("An error occurred while updating the task. Please try again.")
        

def delete_task(task_id):
    """Delete a task by ID."""
    tasks = []
    task_found = False
    try:
        with open("tasks_info.csv", "r", newline='') as file:
            data_reader = csv.reader(file)
            for row in data_reader:
                if len(row) > 0:
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
            print(f"Task with ID {task_id} not found. Please check the ID and try again.")
            
    except IOError as e:
        print("An error occurred while deleting the task. Please try again.")

def view_task_details(task_id):
    """View details of a specific task by ID."""
    try:
        with open("tasks_info.csv", "r", newline='') as file:
            data_reader = csv.reader(file)
            for row in data_reader:
                if row[0] == task_id:
                    print(f"Title: {row[1]}")
                    print(f"Description:\n{row[2]}")
                    return
        print(f"Task with ID {task_id} not found. Please check the ID and try again.")
    except IOError as e:
        print("An error occurred while retrieving the task details. Please try again.")

def unique_ids():
    """Retrieve all unique task IDs."""
    try:
        with open("tasks_info.csv", "r", newline='') as file:
            return {line[0] for line in csv.reader(file) if len(line) > 0}
    except IOError as e:
        print("An error occurred while accessing task data. Please try again.")
        return set()

def create_unique_id():
    """Create a unique task ID."""
    max_task_id = 1000
    id_list = unique_ids()
    while True:
        i = random.randrange(0, max_task_id)
        if not str(i) in id_list:
            return i

def add_task():
    """Add a new task."""
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
    """Display all tasks in a tabular format."""
    all_data = [["Task id", "Task title", "Priority", "Category", "Status"]]
    try:
        with open("tasks_info.csv", "r", newline='') as file:
            data_reader = csv.reader(file)
            for line in data_reader:
                if len(line) > 0:
                    display = [line[0], line[1], line[3], line[4], line[5]]
                    all_data.append(display)
        if len(all_data) > 1:
            return tabulate(all_data, headers="firstrow", tablefmt="fancy_grid")
        else:
            return "Currently no tasks!"
    except IOError as e:
        print("An error occurred while displaying tasks. Please try again.")
        return "Error displaying tasks!"

def complete_task():
    """Prompt user to mark a task as complete."""
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id of the task to mark as complete: ")
        mark_complete(task_id)

def delete_task_prompt():
    """Prompt user to delete a task."""
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id of the task to delete: ")
        delete_task(task_id)

def view_task_prompt():
    """Prompt user to view task details."""
    display = display_tasks()
    print(display)
    if display != "Currently no tasks!":
        task_id = input("Enter task id to view details: ")
        view_task_details(task_id)

def instructions(version):
    """Print usage instructions."""
    print(f"""
Terminal Task Manager
          
In the fast-paced world we live in, staying organized 
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
