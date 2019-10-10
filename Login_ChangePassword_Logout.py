from selenium import webdriver
import time

driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.maximize_window()

driver.get("https://account.targomo.com/login")
driver.implicitly_wait(2)

# Login
driver.find_element_by_id("mat-input-0").send_keys("madhuchandra332019@gmail.com")
driver.find_element_by_id("mat-input-1").send_keys("Test@031020195")
driver.find_element_by_xpath("/html/body/tgm-app/tgm-login/section/div/div[2]/form/div/div[2]/button/span/div/div").click()

# Change password
driver.find_element_by_id("current").send_keys("Test@031020195")
driver.find_element_by_id("mat-input-3").send_keys("Test@031020195")
driver.find_element_by_id("mat-input-4").send_keys("Test@031020195")
driver.find_element_by_xpath("/html/body/tgm-app/tgm-root/div/div/div/div/tgm-settings/tgm-panel-layout/div/div[2]/div/tgm-change-password/tgm-info-card/section/div[1]/div/form/div/div[2]/button/span").click()

# Logout
driver.find_element_by_xpath("/html/body/tgm-app/tgm-root/mat-toolbar/mat-toolbar-row/button/span/span").click()
time.sleep(2)

driver.minimize_window()
driver.close()
driver.quit()
print("Login, password change and logout was successful")