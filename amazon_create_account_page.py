from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/loulouangibeau/Documents/QA-Automation/python-selenium-automation/chromedriver')
service = Service('/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

# Go to Amazon Create Account Page
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.ID, "createAccountSubmit").click()

# Then going to find all objects listed in HW3 part 1
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").is_displayed()

# This test case will verify to see if "Create Account" h1 element is displayed on page
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").is_displayed()

# This test case will also check for the other required elements, but I don't know how to include it in expected results without putting them in different test cases
driver.find_element(By.ID, "ap_customer_name").is_displayed()
driver.find_element(By.ID, "ap_email").is_displayed()
driver.find_element(By.ID, "ap_password").is_displayed()
driver.find_element(By.ID, "ap_password_check").is_displayed()
driver.find_element(By.ID, "ap_password_check").is_displayed()
driver.find_element(By.ID, "continue").is_displayed()
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')]").is_displayed()
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496')]").is_displayed()
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").is_displayed()
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis' and contains(@href,'/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=Y7B7TKJJGDQSCP4SJF18&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')]").is_displayed()

expected_result = "Create Account"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

driver.quit()