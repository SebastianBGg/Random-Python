from time import sleep
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os
from os import path

path = "user-data-dir=C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

options = webdriver.ChromeOptions()
options.add_argument(path)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

driver.get('https://tempail.com/')
email = driver.find_element(By.XPATH, '//*[@id="eposta_adres"]').get_attribute("value")
print(email)
f = open("mails.txt", "w")
f.close
f = open("mails.txt", "a")
f.write(email+"\n")
f.close

print(email)
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.tiktok.com/en/")
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/button").click()
sleep(0.2)
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/div[2]/a/span").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/div[1]/div/div/a/div").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[5]/a").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[1]/div[1]").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[2]").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[2]/div[1]").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[2]/div[2]/div[3]").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[3]/div[1]").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[3]/div[3]/div[2]/div[21]").click()

driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[6]/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[7]/div[1]/input").send_keys("Sebbe123!")
driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[2]/div[1]/div/form/div[8]/div/button").click

driver.switch_to.window(driver.window_handles[0])
sleep(448)
driver.find_element(By.XPATH, "/html/body/section[1]/div[2]/div/div[4]/a[2]").click()
code = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]").text.split()

print(code[0])
sleep(1111111)
