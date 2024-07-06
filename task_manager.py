import argparse
import sys
import csv
import random
from tabulate import tabulate

def save_data(task_id,task_title,task_description,priority,category):
    with open("tasks_info.csv","a") as file:
        data_writer = csv.writer(file)
        data_writer.writerow([task_id,task_title,task_description,priority,category,"Incomplete"])

    print("Task successfully added! ")

def unique_ids():
    id_list = []
    with open("tasks_info.csv","r") as files:
        data_writer = csv.reader(files)    
        for line in data_writer:
            id_list.append(line[0])
    
    return id_list


def create_unique_id():
    id_list = unique_ids()
    while True:
        i = random.randrange(0,1000)
        if len(id_list) == 0:
            return i
        elif not str(i) in id_list:
            return i




def remove_unique_id(id):
    id_collection = set()
    id_collection = unique_ids()
    for i in id_collection:
        if i == id:
            id_collection.remove(i)
            break
        


def add_task():
    task_title = input("Enter Task Title: ")
    task_description = input("Enter description: ")
    priority = input("Enter Priority level (low/medium/high): ")
    category = input("Enter Category (General/personal/work/other): ")
    task_id = create_unique_id()
    save_data(task_id,task_title,task_description,priority,category)


def display_tasks():
    all_data = [["Task id","Task title","Priority","Category","Status"]]
    with open("tasks_info.csv","r") as files:
        data_writer = csv.reader(files)    
        
        for line in data_writer:
            if len(line) >0:
                display = [line[0],line[1],line[3],line[4],line[5]]
                all_data.append(display)

                print(tabulate(all_data,headers="firstrow",tablefmt="fancy_grid"))
            else:
                print("Currently no tasks!")

def complete_task(task_id):
    # Implement logic to mark a task as completed
    pass

def instructions(version):
    print(f"""
Command-Line Task Manager
          
In the fast-paced world we live in, staying organised 
and on top of your tasks is essential for success. 
Introducing command-line Task Manager , your ultimate 
companion in conquering the chaos of daily life for developers. 
          
valid command: python{version} task_manager.py [option]

options:
  -h, --help                Show help message and exit
  --add                     Add a new task
  --display                 Display tasks
  --complete COMPLETE       Mark a task as completed

""")

def main():
    
    version = sys.version_info.major

    parser = argparse.ArgumentParser(description="Command-Line Task Manager")
    parser.add_argument("--add", help="Add a new task", action="store_true")
    parser.add_argument("--display", help="Display tasks", action="store_true")
    parser.add_argument("--complete", help="Mark a task as completed", type=int)

    args = parser.parse_args()

    if args.add:
        add_task()
    elif args.display:
        display_tasks()
    elif args.complete:
        complete_task(args.complete)
    else:
        instructions(version)


if __name__ == "__main__":
    main()
