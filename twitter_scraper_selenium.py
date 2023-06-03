
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

# Actual program:
my_email = 'froncek1231@gmail.com'
username = 'JohnMelody43'
password = 'WStwitter23'

time.sleep(5)
driver.get(url)

time.sleep(5)

#Logging in 
email = driver.find_element(By.XPATH, '//input[@spellcheck="true"]')
email.send_keys(my_email)
email.send_keys(Keys.RETURN)

time.sleep(5)
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

#Searching tweets on Yahoo Finance
search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search Twitter"]')
search_bar.send_keys('Yahoo Finance')
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

#Tweets from Yahoo Finance 
# try with tab index = 0 
span_profile = driver.find_element(By.XPATH, '//div[@class="css-1dbjc4n r-1wbh5a2 r-dnmrzs"]')
profile = span_profile.find_element(By.XPATH, './/a')
profile.click()

time.sleep(5)

tweets_list = []

# Scrolling and collecting tweets along:

#defining the first tweet to appear last in the first view of the page
#afterwards we will have to get rid of duplicates
tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
scroll_element = tweets[-1]

start = time.time()

while True:
    # Scroll inside the specific element
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    # Calculate the new scroll height and check if it has reached the end
    print('No of gathered tweets: ', len(tweets_list))
    if len(tweets_list) > 200:# or new_height == last_height:
        break
    #last_height = new_height

    # Appending tweets from the currently chosen part of the site:
    time.sleep(2)
    tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')  #HERE WE CAN USE EITHER SCRAPY, BS, OR SELENIUM...
    tweets_list.extend([tweet.text for tweet in tweets])

    scroll_element = tweets[-1]
 
end = time.time()

#erasing duplicates should be done after extracting text as it is a dynamic page
print("Time required by Scraper name:", end-start)

time.sleep(3)

print('No. of gathered tweets before erasing duplicates: ', len(tweets_list))
tweets_list = list(set(tweets_list))

time.sleep(3)

print('No. of gathered tweets after erasing duplicates: ', len(tweets_list))

time.sleep(10)

print(tweets_list[14])

time.sleep(10)

# Close browser:
driver.quit()

