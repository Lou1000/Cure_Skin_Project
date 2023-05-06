from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome(executable_path='./chromedriver')
    # # context.browser = webdriver.Safari()
    # # context.browser = webdriver.Firefox()
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver,10)
    # context.app = Application(driver=context.driver)

    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os': 'Windows',
    #     'os_version': '11',
    #     'name': test_name
    # }
    #
    # bs_user = 'loulouangibeau_52cWXg'
    # bs_key = 'qRkE5nyBCNq8Lvnez53n'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path='./chromedriver',
                                      chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

