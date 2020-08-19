from time import *
from selenium import webdriver

started = False

url = 'https://play.typeracer.com/'

driver = webdriver.Chrome()
driver.get(url)
sleep(2)
    
try:
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]').click()
except:
    pass

driver.find_elements_by_css_selector('#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a')[0].click()
print('\n[+] Lobby megtalálva!')
sleep(2)

txt = driver.find_elements_by_css_selector('#gwt-uid-15 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div')[0].text

while not started:
    try:
        for letter in txt:
            driver.find_element_by_class_name('txtInput').send_keys(letter)
            sleep(0.01)
        started = True
    except:
         pass
    
print('\n> Kész!')
driver.quit()