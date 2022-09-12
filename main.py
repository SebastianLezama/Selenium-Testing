from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import env

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://clattor.com/login")
assert "Notimation" in driver.title

login_email = driver.find_element(By.ID, "email")
login_email.clear()
login_email.send_keys(env.USER)

login_pass = driver.find_element(By.ID, "password")
login_pass.clear()
login_pass.send_keys(env.PASS)
login_pass.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col py-3 px-5"))
    )
except:
    driver.quit()

# driver.close()
