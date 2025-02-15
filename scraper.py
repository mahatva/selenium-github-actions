from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

arr =[["FT020601","Apple@123",'30102002'], ["FT022272","Flat-22272",'31071993']]

for x in range(2):
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    url = "https://www.quantman.in/users/sign_in?locale=en"
    driver.get(url)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#flattrade-user-auth"))).click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='flattrade-client-id']"))).send_keys(arr[x][0])
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='btn-flattrade']"))).click()
    time.sleep(3)

    WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH,"//input[@id='input-17']"))).send_keys(arr[x][0])

    WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='pwd']"))).send_keys(arr[x][1])
    totp = arr[x][2]
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='pan']"))).send_keys(totp)
    time.sleep(2)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Login')]"))).click()
    time.sleep(5)
    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[2]")))
        base_url = "https://api.telegram.org/bot6224935224:AAGODWW5hvh0kfFTMlz-MVGquEMtQX26LVY/sendMessage?chat_id=-982268246&text=DoneFlatrade" + str(
            arr[x][0])
        driver.get(base_url)
        time.sleep(5)
        driver.close()
    except:
        base_url = "https://api.telegram.org/bot6224935224:AAGODWW5hvh0kfFTMlz-MVGquEMtQX26LVY/sendMessage?chat_id=-982268246&text=IsuueWithBrokerFailed"
        driver.get(base_url)
        time.sleep(6)
        driver.close()
