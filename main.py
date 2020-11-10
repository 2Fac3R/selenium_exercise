from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data_driver = webdriver.Chrome()

data_driver.get('https://randomtodolistgenerator.herokuapp.com/library')

# List of tasks
task_title_list = data_driver.find_elements_by_class_name("task-title div")

# Login Data
myemail = "genr1818@gmail.com"
mypwd = "pythonselenium"

driver = webdriver.Chrome()

# Login Form
driver.get("https://todoist.com/users/showlogin")

# Email
username = driver.find_element_by_id("email")
username.clear()
username.send_keys(myemail)
# Password
password = driver.find_element_by_name("password")
password.clear()
password.send_keys(mypwd)
# Log In
driver.find_element_by_class_name("submit_btn").click()

# Adding tasks
for task in task_title_list:
    # Waits to be ready
    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "quick_add_task_holder")))
    element.click()

    # Adds a task
    inputElement = driver.switch_to.active_element
    inputElement.send_keys(task.text)
    driver.find_element_by_class_name("ist_button").click()

# End
data_driver.close()
driver.close()