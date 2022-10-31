from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("Selenium Test Case is started")
print("\n")

def browser_function(driver):
    driver.maximize_window()
    driver.get("https://www.python.org/downloads/")
    driver.find_element(By.ID, "id-search-field").send_keys("bla bla")
    driver.find_element(By.NAME, "submit").click()
    result  = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/p')
    displayed = result.is_displayed()
    if displayed is True:
            print("'No results found' text is visible on the screen because desplayed value is",displayed)
    refresh = driver.refresh()

    result = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > p")
    print('The result of found is' , result.text )
    get_title = driver.title
    print("The title of page is ", get_title )
    get_url = driver.current_url
    print("The current url of page is ", get_url)
    print("Selenium Test Case ended")
    driver.close()

browser_function(driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()))
browser_function(driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()))
