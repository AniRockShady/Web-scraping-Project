from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import re
import csv
import pandas as pd
from tqdm import tqdm

# Init:
gecko_path = '/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options=options, service=ser)

url = 'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/'

#Asking driver the fetch tomatometer movie ranking site:
driver.get(url)
time.sleep(2)

start = time.time()
#Accepting cookies
try:
    accept_button = driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]') 
    accept_button.click()
except:
    pass

links = []

titles = driver.find_elements(By.CLASS_NAME, 'article_movie_poster')

#Getting 100 links to movies
for title in titles:
    a = title.get_attribute("href")
    movie_link = re.search(r"https?://[\w\-\.]+(/\S*)?", a)
    if movie_link:
        links.append(movie_link.group())

print('Number of scraped movie links: ',len(links))
# Defininig CSV to store scraped info
df_info = []

for i in tqdm(range(len(links)), desc = 'Processing'):
    link = links[i]
    driver.get(link)
    title = driver.find_element(By.XPATH, '//h1[@class="title"]').text
    year = driver.find_element(By.XPATH, '//p[@class="info"]').text[:4]
    tomatometerscore = driver.find_element(By.XPATH, '//score-board[@id="scoreboard"]').get_attribute('tomatometerscore')

    df_info.append({'Link': str(link), 'Title': title, 'Year': year, 'Rating': tomatometerscore})

end  = time.time()

print(f"Time required by Selenium scraper: {end-start} seconds", )

#Transforming to dataframe format 
df_info = pd.DataFrame(df_info)

df_info

# Quit the driver
driver.quit()