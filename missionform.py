from datetime import date
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# enable headless mode in Selenium
# options = Options()
# options.add_argument('--headless=new')
def missionform(commanding_officer):
    print(commanding_officer)
    browser = webdriver.Chrome(
    )

    browser.get('https://docs.google.com/forms/d/e/1FAIpQLScPx6zO9Enl8lzlwl-uDNIT-hqJdnRiUG9GpmKw90z2sJ0Tzg/viewform')

    time.sleep(2)
    id = "613016034722709524"
    name = "Dick Blackbird"
    
    start_date = browser.find_element(By.XPATH, "(//input[@type='date'])[1]")  # Find the search box
    finish_date = browser.find_element(By.XPATH, "(//input[@type='date'])[2]")
    start_time_hour = browser.find_element(By.XPATH, "(//input[@aria-label='Hour'])[1]")
    start_time_minute = browser.find_element(By.XPATH, "(//input[@aria-label='Minute'])[1]")
    start_time_period = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]')
    finish_time_hour= browser.find_element(By.XPATH, "(//input[@aria-label='Hour'])[2]")
    finish_time_minute = browser.find_element(By.XPATH, "(//input[@aria-label='Minute'])[2]")
    finish_time_period = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]')
    first_page_next_button = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
   



    today = date.today()
    now = datetime.now()
    hours = now.hour

    # Determine if it's AM or PM
    if hours == 0:
        start_period = "PM"
    else:
        start_period = "AM"
    period = "AM" if hours < 12 else "PM"
    print(start_period)
    # Convert to standard time
    hours = hours if hours <= 12 else hours - 12
    hours = 12 if hours == 0 else hours
    start_hour = hours-1


    start_date.send_keys(f"{today}")
    finish_date.send_keys(f"{today}")
    start_time_hour.send_keys(f"{start_hour}")
    start_time_minute.send_keys(f"{now.minute}")
    start_time_period.send_keys(f"{start_period}")
    finish_time_hour.send_keys(f"{hours}")
    finish_time_minute.send_keys(f"{now.minute}")
    finish_time_period.send_keys(f"{period}")
    first_page_next_button.click() 
    time.sleep(2)
    discord_ID= browser.find_element(By.XPATH, "(//input[@type='text'])[1]")
    alias = browser.find_element(By.XPATH, "(//input[@type='text'])[2]")
    commandingOfficer = browser.find_element(By.XPATH, "(//input[@type='text'])[3]")
    second_page_next_button = browser.find_element(By.XPATH, "(//span[contains(text(),'Next')])[1]")

    

    discord_ID.send_keys(f"{id}")
    alias.send_keys(f"{name}")
    commandingOfficer.send_keys(f"{commanding_officer}")
    second_page_next_button.click()
    time.sleep(2)

    submit_button = browser.find_element(By.XPATH, "(//span[contains(text(),'Submit')])[1]")
    
    submit_button.click()


def run():
    commanding_officer = input('commanding officer : ')

    missionform(commanding_officer)

run()