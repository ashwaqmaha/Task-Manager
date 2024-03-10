import argparse
import sys

def add_task():
    # Implement logic to add a new task
    print("Testing to see connection")

def display_tasks():
    # Implement logic to display tasks
    pass

def complete_task(task_id):
    # Implement logic to mark a task as completed
    pass

def instructions(version):
    print(f"""
Command-Line Task Manager
          
In the fast-paced world we live in, staying organised 
and on top of your tasks is essential for success. 
Introducing command-line Task Manager , your ultimate 
companion in conquering the chaos of daily life. 
          
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
