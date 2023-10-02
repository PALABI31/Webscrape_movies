from bs4 import BeautifulSoup
import requests
import re 

page_to_scrape = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


titles = soup.findAll("h3", attrs={"class":"_h3_cuogz_1"})

for title in titles:
    new = title.text.strip()

    print(new)



with open('imdb.txt','w') as pull:
    for title in titles:
        new = title.text.strip()
        cleaned_text = re.sub(r'[^\x00-\x7F]+', '', new)
        pull.write(cleaned_text + '\n')



