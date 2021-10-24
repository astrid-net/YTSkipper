from selenium import webdriver
from time import sleep
import chromedriver_autoinstaller

def skipad(driver):
    while True:
        
        sleep(0.3)
        try:
            driver.find_element_by_xpath('//button[@class="ytp-ad-skip-button ytp-button"]').click()
            driver.find_element_by_xpath('//tp-yt-paper-button[@id="button"]').click()
            print('ok')
        except Exception as e:
            if 'window was already closed' in str(e):
                break
            else:
                continue
            
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

skipad(driver)
