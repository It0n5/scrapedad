import requests
from rich import *
import re
from string import *

def scrapePaths(path):
    match = re.findall(r'\/?@\S+', str(path))
    #q = str(match).split(',',-1)
    d = str(match).replace(";case","")
    y = str.strip(str(d).replace("\\",""))
    c = str.strip(str(y).replace("}",""))
    v = str.strip(str(c).replace("\"",""))
    r = str(v).split(',',)
    print(r)
def scrapePage(url):
    t = str(url)
    pageText = requests.get(t)
    print(str(pageText.status_code))
    #print(str(pageText.content))
    scrapePaths(pageText.content)
  

if __name__ == "__main__":
    ur = input("Please enter a url: ")
    scrapePage(str(ur))




#stuff