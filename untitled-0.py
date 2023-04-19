# untitled-0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


wait = WebDriverWait(browser, 20)

element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element(By.ID, 'book').click()

x = int(browser.find_element(By.ID, 'input_value').text)
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.XPATH, '//button[@id="solve"]').click()



input()
browser.close()
