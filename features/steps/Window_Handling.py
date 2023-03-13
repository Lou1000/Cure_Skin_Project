from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from behave import given, when, then

privacy_policy_btn = (By.XPATH, "//a[@class='help-display-cond help-display-cond-hidden help-display-cond-rule-platform-DesktopBrowser help-display-cond-rule-platform-MobileBrowser help-display-cond-rule-platform-PhoneAppAndroid help-display-cond-rule-platform-TabletAppAndroid']")

@given("Open Amazon T&C page")
def open_tc_page (context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def storing_windows (context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when("Click on Amazon Privacy Notice link")
def click_privacy_policy (context):
    clicking_priv_pol = context.driver.find_elements(*privacy_policy_btn)
    clicking_priv_pol[0].click()


@when("Switch to the newly opened window")
def switching_window (context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('\nALL WINDOWS', windows)

    context.driver.switch_to.window(windows[1])
    context.current_window = context.driver.current_window_handle
    print('\nAFTER WE SWITCHED', windows[1])

@then("Verify Amazon Privacy Notice page is opened")
def verify_window_opened (context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7'))

@then("User can close new window and switch back to original")
def switching_back (context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
