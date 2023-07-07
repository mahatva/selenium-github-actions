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

arr =[["FT020601","Apple@123",'XK3U43T7MJW7H62T6443AX7BHM5B3IK3'], ["FT022272","Flat-22272",'WKK336STJDPV7I2735CN32475N24TX5K']]

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
    totp = pyotp.TOTP(arr[x][2])
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='pan']"))).send_keys(totp.now())
    time.sleep(2)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Login')]"))).click()
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='goto-btn btn btn-success text-nowrap btn-pill']")))
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
