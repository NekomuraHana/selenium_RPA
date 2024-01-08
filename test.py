from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.co.jp/")


serach = driver.find_element(By.NAME,"q")
serach.send_keys("hell world")
serachButton = driver.find_element(By.NAME,"btnK")
driver.execute_script('arguments[0].click();', serachButton)
