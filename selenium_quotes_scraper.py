from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.get('https://ru.citaty.net/avtory/vladimir-vladimirovich-putin/')

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

html = driver.page_source   #для использования далее в BS
soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('h3', class_=['blockquote-text'])

for quote in result:
    with open('putin_quotes.txt', 'a', encoding='utf-8') as f:
        f.write(quote.text.replace('„','').replace('“','') + '\n')

driver.close()