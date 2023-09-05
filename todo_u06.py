tasks = []

exit = False

while not exit:
  print("\nMenu")
  print("a - Add Task")
  print("v - View Tasks")
  print("r - Remove Task")
  print("q - Quit")

  choice = input("Enter your choice: ")

  if choice == "a":
    task = input("Add Task: ")
    tasks.append(task)
    print("Task added!")
  elif choice == "v":
        if not tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
  elif choice == "r":
      if not tasks:
        print("There is no task to remove")
      else:
        remove_task = input("Enter the task that you want to remove: ")
        tasks.remove(remove_task)
        print("Task removed!")
  elif choice == 'q':
      print("Exiting the to-do list application. Goodbye!")
      break
