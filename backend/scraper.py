import requests
from bs4 import BeautifulSoup

def scrape_scholarships():
    url = "https://example.com/scholarships"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    scholarships = []
    for item in soup.find_all("div", class_="scholarship"):
        title = item.find("h2").text
        link = item.find("a")["href"]
        scholarships.append({"title": title, "link": link})
    
    return scholarships
