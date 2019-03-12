from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
#def login():
driver = webdriver.Chrome()
driver.get("http://localhost:8080/examsys/login.thtml")
driver.find_element_by_name('username').send_keys('hujianming')
driver.find_element_by_name('userpass').send_keys('hujianming123')
sel=driver.find_element_by_xpath('/html/body/div/div/table/tbody/tr[3]/td/select')
sel.click()
Select(sel).select_by_visible_text('管理员')
sleep(10)
driver.find_element_by_class_name('tm_btn').click()

print(capitalize('abc'))
#driver.quit()

#driver.quit()
