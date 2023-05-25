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

account = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='email']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='pass']")))
account.send_keys("patrick11534@yahoo.com.tw")
password.send_keys("lin880005")
"""div = driver.find_element(By.NAME,"login")
div.click()
"""
password.submit()
cookie = driver.get_cookies()
print(cookie)
jsck = json.dumps(cookie)
with open("fbpass.json","w") as f:
    f.write(jsck)

time.sleep(999)

