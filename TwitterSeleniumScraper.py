###############################
# YahooFinance Tweets Scraper #
###############################

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
options.headless = True
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://twitter.com/i/flow/login'

#Dummy twitter account
my_email = 'froncek1231@gmail.com'
username = 'JohnMelody43'
password = 'WStwitter23'

time.sleep(3)
driver.get(url)

time.sleep(3)

#Logging in with login/email/password
print("Logging in")
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

time.sleep(3)

#Searching Yahoo Finance in the search-bar
search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search Twitter"]')
search_bar.send_keys('Yahoo Finance')
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

#Reaching Yahoo Finance profile
span_profile = driver.find_element(By.XPATH, '//div[@class="css-1dbjc4n r-1wbh5a2 r-dnmrzs"]')
profile = span_profile.find_element(By.XPATH, './/a')
profile.click()

time.sleep(5)

tweets_list = []

#Scrolling and collecting Tweets along.
#Scrolling element is the last available tweet
tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
scroll_element = tweets[-1]

start = time.time()

while True:
    # Scroll inside the specific element
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    # Calculate the new scroll height and check if it has reached the end
    print('No of gathered tweets: ', len(tweets_list))
    if len(tweets_list) > 30:
        break

    # Appending tweets from the currently chosen part of the site:
    time.sleep(2)
    tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')  #HERE WE CAN USE EITHER SCRAPY, BS, OR SELENIUM...
    tweets_list.extend([tweet.text for tweet in tweets])

    scroll_element = tweets[-1]
 
end = time.time()

#erasing duplicates should be done after extracting text as it is a dynamic page
print("Time required to scrape tweets:", end-start)

time.sleep(2)

print('No. of gathered tweets before erasing duplicates: ', len(tweets_list))
tweets_list = list(set(tweets_list))

time.sleep(2)

print('No. of gathered tweets after erasing duplicates: ', len(tweets_list))

time.sleep(2)

print("5th of gathered tweets: ", tweets_list[4])

time.sleep(2)

# Close browser:
driver.quit()

