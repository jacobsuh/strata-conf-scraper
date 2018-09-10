import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

csv_file = open("strata2018.csv", "w")
headers = "Company Name, Website, Location"
csv_file.write(headers + "\n")

# strata_link = "https://conferences.oreilly.com/strata/strata-ny/public/content/sponsors"
# browser = webdriver.Chrome()
# browser.get(strata_link)

# exhibitors_button = browser.find_element_by_link_text("Exhibitors")
# exhibitors_button.click()

strata_link = "https://conferences.oreilly.com/strata/strata-ny/public/content/sponsors"
r = requests.get(strata_link)
source = r.text

# source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

for i in soup.findAll("div", "sponsor-blurb"):


    test = i.findAll("a", text=True)
    cos_name = test[0].text
    url = test[0]['href']

    csv_row = [cos_name, url]
    data = ",".join(csv_row)
    csv_file.write(data + "\n")

csv_file.close()