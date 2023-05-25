from bs4 import BeautifulSoup

path ="web.html"
with open (path,"r",encoding="utf-8") as f:
    soup  = BeautifulSoup(f.read(),"html") 

#print(soup.prettify())
print(soup.title.text)
print(soup.find("h1",class_="abc"))
print(soup.select(".abc"),5)
print(soup.select("h1[class=job]"),6)
print(soup("a"))
print(soup.h2.text)