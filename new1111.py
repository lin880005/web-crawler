from selenium import webdriver
from selenium.webdriver.common.by import By #選取器
from selenium.webdriver.support.wait import WebDriverWait #網站等待
from selenium.webdriver.support import expected_conditions as EC #元素狀態判別
from selenium.webdriver.chrome.options import Options #瀏覽器設定
from bs4 import BeautifulSoup
import json
import time

options = Options()
#options.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values":{"notifications":2}} #創建設定
options.add_experimental_option("prefs",prefs) #合併設定

driver = webdriver.Chrome("chromedriver.exe",options=options)
driver.get("https://www.1111.com.tw/")

sreach = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='ks']")))
div = driver.find_element(By.ID,"searchjobBtn")
sreach.send_keys("大數據工程師")
div.click()

soup = BeautifulSoup(driver.page_source,"html.parser")


roll =0
count = 0
page = soup.find_all("div",class_="srh-body__result-item srh-body__result-item--loaded")

while page.find_all("div",class_="body-wrapper") !=0:
    roll+=100
    for job in page.find_all("div",class_="body-wrapper"):
        count+=1
        print(job.h5.text)                                          # 職缺名稱
        print(job.find("div", class_="job_item_info").a["href"])    # 職缺網址
        print(job.h6.text)                                          # 公司名稱
        print(job.find("a", class_="job_item_detail_location mr-3 position-relative").text)          # 地區
        print(job.find("div", class_="job_item_detail_salary ml-3 font-weight-style digit_6").text)  # 薪資
        print("==============================================")
    
    driver.execute_script(f"window.scrollTo(0,{str(roll)})")
print(f"工作筆數總共:{count}筆")

time.sleep(100)
