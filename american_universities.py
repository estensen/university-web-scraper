from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("http://www.ntnu.no/international/usa/tableusacanada.htm") as url:
    r = url.read()

soup = BeautifulSoup(r, "html.parser")

filename = "american_universities.txt"
with open(filename, "w") as f:
    rows = soup.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if cols and cols[0].get_text() == "USA":
            f.write(cols[1].get_text()+"\n")
