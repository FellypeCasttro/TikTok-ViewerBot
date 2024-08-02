from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import os
import ctypes

# Configurações do ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Atualize para usar webdriver_manager para gerenciar o ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Inicialize o WebDriver com as opções corretas
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=chrome_options)

print("Welcome to Flynn's Tiktok Viewer Bot.")
print("Press (ctrl + c) to exit it")
urlVar = input("Enter TikTok URL:\n")

driver.get("https://zefoy.com/")
os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
screenshot = driver.save_screenshot('captcha.png')
img = Image.open('captcha.png')
img.show()

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

captchaString = input("Input Captcha?\n")

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

inputCaptcha = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input')
inputCaptcha.send_keys(captchaString)
inputCaptcha.send_keys(Keys.ENTER)

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

clickbutton = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[5]/div/button').click()

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

urlInput = driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/input')
urlInput.send_keys(urlVar)

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

i = 1
ammount = 0

while i == 1:
    time.sleep(5)
    urlInput = driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/div/button').click()
    time.sleep(3)

    try:
        driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[1]/div/form/button').click()
        ammount += 1000
        os.system(f"title {ammount}" if os.name == 'nt' else '')  # Atualiza o título da janela do terminal no Windows
    except NoSuchElementException:
        getTextAll = driver.find_element(By.XPATH, '//*[@id="gettimesv"]')
        getText = getTextAll.text
        if getText != "Next Submit: READY....!":
            text1, text2 = getText.split('minute(s)', 1)
            text1 = text1.replace('Please wait ', '').strip()
            text2 = text2.replace(' seconds for your next submit!', '').strip()
            intTime = (int(text1) * 60) + int(text2)
            while intTime > 0:
                mins, secs = divmod(intTime, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                intTime -= 1
        else:
            print("Ready :)")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
