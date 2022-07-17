from http import server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pa

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\Usuario\Downloads\chromedriver.exe" # here goes your chromedriver location

# opens website in chromedriver (headless mode)
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# web scraping with xpath
containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text # by './' we avoid writing '//div[@class="teaser__copy-container"]' again
    subtitle = container.find_element(by='xpath', value='./a/p').text 
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

print(titles)
print(subtitles)
print(links)

my_dict = {'title': titles, 'subtitle':subtitles, 'link':links}
news = pa.DataFrame(my_dict)
news.to_csv("news-headless-mode.csv")

driver.quit()