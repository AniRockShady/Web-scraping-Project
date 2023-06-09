# 100 BEST MOVIES
from urllib import request
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd



url = 'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/?fbclid=IwAR0BOUz-htWPJZVuHUzImAXxxRD3vfaJjSieIf4Thm8p2xx9C1Ldz-UgGJA'
page = requests.get(url)
soup = BS(page.text, 'lxml')

#print(soup)
d = pd.DataFrame({'Links': [''],'Titles': [''], 'Rating': [''], 'Year': [''], 'Director': ['']})

data = {'Links': []}

postings = soup.find_all('div', class_ = 'row countdown-item')
#print(postings)

for post in postings:
    link = post.find('a',class_ = 'article_movie_poster').get('href')
    data['Links'].append(link)
df =pd.DataFrame(data)

#df.to_csv('C:/Users/mraer/Desktop/UW/Semester-2/Webscrapping/Webscrapping-Project/netflix.csv')

for links in df['Links']:
    print(links)

    html = request.urlopen(df['Links'])
    bs = BS(html.read(), 'html.parser')
    
    titles = post.find_all('div',class_ = 'title')
    for t in titles:
        title = t.find('a').text
        print(title)
    # rating = post.find('span', class_ = 'percentage').text
    # print(rating)
    # year_elements = post.find_all('span',class_ = 'subtle start-year')
    # years = [year_element.text.strip('()') for year_element in year_elements]
    # for year in years:
    #     print(year)
    # directors = post.find_all('div',class_ = 'info director')
    # for director in directors:
    #     name = director.find('a').text
    #     print(name)
    df = df.append({'Links': link,'Titles': title})#, 'Rating': rating,'Year': year, 'Director': name},ignore_index=True)

