from bs4 import BeautifulSoup
import requests

#Url lists
url = []

#function
def scrape(site):
    r = requests.get(site)
    
    #converting text
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswitch("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)

#calling my function
if __name__ == "__name__":
    site = "http://obertzitha.42web.io/?i=2"
    scrape(site)
    