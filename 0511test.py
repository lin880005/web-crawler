import requests
from bs4 import BeautifulSoup

url = "https://www.104.com.tw/jobs/search/?keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0"
res = requests.get(url)
soup=BeautifulSoup(res.text)

for job in soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item js-job-item"):
    print(job["data-job-name"])
    print(job["data-cust-name"])
    print(job("li")[2].text)
    if job.find('div',class_="job-list-tag b-content").select('span')==[]:
        print(job.find('div',class_="job-list-tag b-content").a.text)
    else:
        print(job.find('div',class_="job-list-tag b-content").span.text)
    print("https:"+job("a")[0]["href"])
    print("=============================================")
