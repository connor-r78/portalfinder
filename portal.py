from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random

link = "https://irt.crschmidt.net/panoclick.html?lat=51.498519&lng=12.643872&pano=CAoSFkNJSE0wb2dLRUlDQWdJREU5NUxhUFE."

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get(link)
time.sleep(10)

canvas = driver.find_element(By.TAG_NAME, "canvas")
location = canvas.location
size = canvas.size
print(f"Canvas location: {location}, size: {size}")

actions = ActionChains(driver)

for i in range(100):
    x = random.randint(0, int(size['width']) - 1)
    y = random.randint(0, int(size['height']) - 1)
    
    print(f"[{i+1}/100] Clicking canvas at ({x}, {y})")
    try:
        actions.move_to_element_with_offset(canvas, x, y).click().perform()
    except Exception as e:
        print(f"Error clicking at ({x}, {y}): {e}")

try:
    execute_button = driver.find_element(By.ID, "executeButton")
    execute_button.click()
    print("\nClicked the execute button.")
except Exception as e:
    print(f"\nCould not find or click execute button: {e}")
