from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()

sleep(1)
yes_radio = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label')
yes_radio.click()
file.close()