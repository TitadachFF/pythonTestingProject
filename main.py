import time
from selenium import webdriver

# driver = webdriver.Chrome(executable_path = "/Users/naruaponsuwanwijit/Desktop/chromedriver")


s = Service('D:\\webdriver\\chromedriver.exe'')
driver = webdriver.Chrome(service=s)


driver.get("https://sc.npru.ac.th/")
time.sleep(2)
driver.close()
