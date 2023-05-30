
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass
import datetime

# Init:
ser = Service('/usr/local/Cellar/geckodriver')
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://twitter.com/i/flow/login'

start = time.time()

# Actual program:
my_email = 'froncek1231@gmail.com'
username = 'JohnMelody43'
password = 'WStwitter23'

driver.get(url)
time.sleep(3)

#Logging in 
email = driver.find_element(By.XPATH, '//input[@spellcheck="true"]')
email.send_keys(my_email)
email.send_keys(Keys.RETURN)

time.sleep(3)
try:
    pass_elem = driver.find_element(By.XPATH, '//input[@type="password"]')
    pass_elem.send_keys(password)
    pass_elem.send_keys(Keys.RETURN)

except:
    user = driver.find_element(By.XPATH, '//input[@spellcheck="false"]')
    user.send_keys(username)
    user.send_keys(Keys.RETURN)

    time.sleep(3)

    pass_elem = driver.find_element(By.XPATH, '//input[@type="password"]')
    pass_elem.send_keys(password)
    pass_elem.send_keys(Keys.RETURN)


#Searching tweets on Yahoo Finance
search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search Twitter"]')
search_bar.send_keys('Yahoo Finance')
search_bar.send_keys(Keys.RETURN)

#Tweets from Yahoo Finance 
# try with tab index = 0 
profile = driver.find_element(By.XPATH, '//*[contains(text(), "Yahoo Finance")]')
profile.click

#From this moment on we can either utilise bs.soup or scrapy or selenium to scrape tweets from the site

# Close browser:
#driver.quit()

#css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu

'''
time.sleep(2)

password = driver.find_element(By.XPATH, '//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your email:')
password.send_keys(my_pass)

time.sleep(2)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()

time.sleep(9)


searchbar

chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside[1]/div/div[1]/div[2]/ul/li[2]/button')
chat.click()

time.sleep(4)

bot_test_chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside[2]/div[2]/div[2]/ul/li[1]/h5')
bot_test_chat.click()

time.sleep(4)

timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('Hello I am little bot!\n')
time.sleep(0.3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('I messaged at: ' + timestamp + '\n')
time.sleep(0.3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/textarea').send_keys('I was run by: ' + my_email + '\n')

# Pressing enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()



end = time.time()

print("Time required by Scraper name:", end-start)

time.sleep(10)

# Close browser:
driver.quit()
'''
