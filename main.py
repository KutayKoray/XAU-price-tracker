from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

API_KEY = "api_key" # Telegram bot API key
CHAT_ID = "chat_id" # Telegram chat id

price_list = [] # store prices
expected_percent = 1 # send %1 drop notification
time_interval_seconds = 60 # check every 60 seconds

def notify_user(message):
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Bildirim başarıyla gönderildi!")
    else:
        print("Bildirim gönderilemedi. Hata:", response.json())

def check_price_drop(price_list, new_price, expected_percent):
    for old_price in price_list:
        expected_value = ((old_price * expected_percent))
        if new_price <= expected_value:
            return True, expected_value, old_price
    return False, None, None

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

url = "https://tr.investing.com/currencies/xau-usd"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='instrument-price-last']")))
print("Sayfa yüklendi")

def get_gold_price():
    try:
        price_element = driver.find_element(By.CSS_SELECTOR, "[data-test='instrument-price-last']")
        print("Fiyat elementi:", price_element.text)
        price = price_element.text.replace(',', '')
        formatted_price = float(price.replace('.', '')[:4])
        return formatted_price
    except Exception as e:
        print("Fiyat alınamadı:", e)
        return None

for i in range(time_interval_seconds):
    time.sleep(1)
    price = get_gold_price()
    if price:
        print("Altın fiyatı:", price)
        if price_list:
            is_dropped, drop_percent, old_price = check_price_drop(price_list, price, expected_percent)
            if is_dropped:
                notify_user(f"Altın fiyatı {old_price} değerinden {drop_percent:.2f}% düştü! Son fiyat: {price}")

        price_list.append(price)
    else:
        print("Tekrar deniyor...")
        time.sleep(5)
