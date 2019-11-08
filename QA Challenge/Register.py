from selenium import webdriver
import time

driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")

driver.get("https://account.targomo.com/signup")
driver.implicitly_wait(5)

driver.find_element_by_id("hs-eu-confirmation-button").click()

# User Information page
driver.find_element_by_id("mat-select-0").send_keys("pro") # Plan
driver.find_element_by_id("mat-input-0").send_keys("Madhu") # First Name
driver.find_element_by_id("mat-input-1").send_keys("Chandra") # Last Name
driver.find_element_by_id("mat-input-2").send_keys("rattettacut-2388@yopmail.com")  # Email (yoyodod@appmail24.com)
driver.find_element_by_id("mat-select-1").send_keys("India") # Country
driver.find_element_by_id("mat-input-3").send_keys("Madhu@123456") # Password
driver.find_element_by_id("mat-input-4").send_keys("Madhu@123456") # Confirm Password
driver.find_element_by_xpath("//*[@id='cdk-step-content-0-0']/form/div[4]/button/span").click() # Next button

# Billing Information page
driver.find_element_by_id("mat-input-8").send_keys("Madhu") # Billing Name
driver.find_element_by_xpath("/html/body/tgm-app/tgm-sign-up/div/mat-horizontal-stepper/div[2]/div[2]/form/div[1]/div[1]/mat-checkbox/label/div").click() # Checkbox - Billing Email is different from account Email
driver.find_element_by_id("mat-input-15").send_keys("madhuchandr@gmail.com") # Billing Email
driver.find_element_by_id("mat-input-9").send_keys("Eisenhutweg") # Billing Address Line 1
driver.find_element_by_id("mat-input-10").send_keys("Johannisthal") # Billing Address Line 2
driver.find_element_by_id("mat-input-11").send_keys("Berlin") # Billing City
driver.find_element_by_id("mat-input-12").send_keys("Berlin") # Billing Region
driver.find_element_by_id("mat-input-13").send_keys("12487") # Billing Postal Code
driver.find_element_by_id("mat-select-4").send_keys("Germany") # Billing Country
driver.find_element_by_xpath("//*[@id='cdk-step-content-0-1']/form/div[2]/button[2]/span").click() # Next button

# Background page
#driver.find_element_by_xpath("//*[@id='cdk-step-content-0-2']/button/span").click() # No thanks, I'll just continue
driver.find_element_by_id("mat-select-2").send_keys("Other") # How did you learn about us?
driver.find_element_by_id("mat-select-3").send_keys("Retail") # Select Industry
driver.find_element_by_id("mat-input-5").send_keys("Test automation - Selenium Webdriver, PyCharm IDE, Python") #User Description
driver.find_element_by_id("mat-input-6").send_keys("Targomo GmbH, Berlin, Germany")
driver.find_element_by_id("mat-input-7").send_keys("https//www.targomo.com")
driver.find_element_by_xpath("//*[@id='cdk-step-content-0-2']/form/div[2]/button[2]/span").click() # Next button

# Recap page
driver.switch_to.frame("__privateStripeFrame5")
driver.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[1]/span[2]/span/input').send_keys("5546370226859020") # Card Number
driver.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[2]/span/span/input').send_keys("0420")# MM and YY
driver.find_element_by_xpath('//*[@id="root"]/form/div/div[2]/span[3]/span/span/input').send_keys("000")# CVC
driver.switch_to.default_content()
driver.find_element_by_id("mat-input-14").send_keys("Madhu Chandra") # Cardholder Name
driver.find_element_by_xpath("//*[@id='mat-checkbox-1']/label/div").click() # Checkbox - Keep me informed of what is new and improved.
driver.find_element_by_xpath("//*[@id='mat-checkbox-2']/label/div").click() # Checkbox - I have read and accept the terms of use and privacy policy.
# driver.find_element_by_xpath("//*[@id='cdk-step-content-0-3']/form/div[2]/button/span").click() # Submit Registration

print("New user account registration is successful")