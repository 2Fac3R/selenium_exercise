from TaskHandler import TaskHandler

def main():
  try:
    tasks = TaskHandler('https://randomtodolistgenerator.herokuapp.com/library')
    task_list = tasks.get_tasks()

    tasks.login('https://todoist.com/users/showlogin','email@gmail.com', 'password')
    tasks.add_tasks(task_list)

  finally:
    del tasks

if __name__ == "__main__":
  main()