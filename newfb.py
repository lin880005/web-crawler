from selenium import webdriver
from selenium.webdriver.common.by import By #選取器
from selenium.webdriver.support.wait import WebDriverWait #網站等待
from selenium.webdriver.support import expected_conditions as EC #元素狀態判別
from selenium.webdriver.chrome.options import Options #瀏覽器設定
import json
import time

#瀏覽器設定
options = Options()
#options.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values":{"notifications":2}} #創建設定
options.add_experimental_option("prefs",prefs) #合併設定

driver = webdriver.Chrome("chromedriver.exe",options=options)
driver.get("https://zh-tw.facebook.com/")

f1 = open("fbpass.json")
cookies = json.loads(f1.read())

for coolie in cookies:
    driver.add_cookie(coolie)
f1.close()
driver.refresh()

time.sleep(60)