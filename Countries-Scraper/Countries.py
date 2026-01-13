from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

countries = soup.find_all("div", class_="country")

country_names = []
capitals = []
populations = []
areas = []

for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()
    area = country.find("span", class_="country-area").text.strip()

    country_names.append(name)
    capitals.append(capital)
    populations.append(population)
    areas.append(area)

df = pd.DataFrame({
    "Country": country_names,
    "Capital": capitals,
    "Population": populations,
    "Area": areas
})

df.to_csv("countries.csv", index=False)

print("Scraping completed. File saved as countries.csv")
