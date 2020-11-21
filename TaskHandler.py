from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TaskHandler:

  def __init__(self, tasks_source):
    # Headless - No browser windows open
    options = Options()
    options.headless = True
    # Source of tasks 
    self.driver = webdriver.Chrome(options=options)
    self.driver.get(tasks_source)
    # Todoist driver
    self.driver2 = webdriver.Chrome()
    
  # List of tasks
  def get_tasks(self):
    return self.driver.find_elements(By.CLASS_NAME, "task-title div")
  
  # Add tasks
  def add_tasks(self, tasks_list):
    for task in tasks_list:
      # Waits to be ready
      element = WebDriverWait(self.driver2, 20).until(EC.element_to_be_clickable((By.ID, "quick_add_task_holder")))
      element.click()

      # Adds a task
      inputElement = self.driver2.switch_to.active_element
      inputElement.send_keys(task.text)
      self.driver2.find_element(By.CLASS_NAME, "ist_button").click()

  # Login Form
  def login(self, loginForm, myEmail, myPassword):
    self.driver2.get(loginForm)
    # Email
    username = self.driver2.find_element(By.ID, "email")
    username.clear()
    username.send_keys(myEmail)
    # Password
    password = self.driver2.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(myPassword)
    # Log In
    self.driver2.find_element(By.CLASS_NAME, "submit_btn").click()

  def __del__(self):
    self.driver.quit()
    self.driver2.quit()