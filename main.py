import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/blakehendricks/Downloads/chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.surveymonkey.com/r/GARDENS_HEALTH_SCREENING')

# 1st question
nxt_box = driver.find_element_by_id('441855748_2929673042').send_keys("Blake Hendricks")
time.sleep(.5)
nxt_box = driver.find_element_by_id('441855748_2929673043')
nxt_box.send_keys("FOH")
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441855748-ok').click()
time.sleep(.5)

# 2nd you traveled on a flight
nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[4]/div/div/fieldset/div/div/div[2]/div/label').click()
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441856231-ok')
nxt_btn.click()
time.sleep(.5)

# 3rd question
nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[6]/div/div/fieldset/div/div/div[2]/div/label').click()
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441856622-ok')
nxt_btn.click()
time.sleep(.5)

# where question
nxt_box = driver.find_element_by_id('441856884_2929677810')
nxt_box.send_keys("Home")
time.sleep(.5)
nxt_box = driver.find_element_by_id('441856884_2929677811')
nxt_box.send_keys("Yesterday")
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441856884-ok')
nxt_btn.click()
time.sleep(.5)

# do you know someone question
nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[10]/div/div/fieldset/div/div/div[2]/div/label')
nxt_check_box.click()
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441857184-ok')
nxt_btn.click()
time.sleep(.5)
# temperature question
temp_list = [98.6, 97.5, 96.2, 98.3, 95.8]
random_num = random.choice(temp_list)
nxt_box = driver.find_element_by_id('441858148').send_keys(str(random_num))
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441858148-ok')
nxt_btn.click()
time.sleep(.5)

# FIX TIME FORMAT
nxt_box = driver.find_element_by_id('441858791_2929672004_DMY')
now = datetime.now()
current_time = now.strftime("%m/%d/%Y")
nxt_box.send_keys(current_time)
time.sleep(.5)

nxt_box = driver.find_element_by_id('441858791_2929672004_H')
now = datetime.now()
current_time = now.strftime("%I")
nxt_box.send_keys(current_time)
time.sleep(.5)
nxt_box = driver.find_element_by_id('441858791_2929672004_M')
now = datetime.now()
current_time = now.strftime("%M")
nxt_box.send_keys(current_time)
time.sleep(.5)
nxt_box = driver.find_element_by_id('441858791_2929672004_AM')
now = datetime.now()
current_time = now.strftime("%p")
nxt_box.send_keys(current_time)
time.sleep(.5)
nxt_btn = driver.find_element_by_id('441858791-ok')
nxt_btn.click()
time.sleep(.5)

# question 8
nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[16]/div/div/fieldset/div/div/div[1]/div/label')
nxt_check_box.click()
time.sleep(.5)

# ERROR: Finding question 9 element. Deploying explicit wait to find element. Try implicit wait

nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[18]/div/div/fieldset/div/div/div[1]/div/label')
nxt_check_box.click()
time.sleep(.5)

# question 10
nxt_check_box = driver.find_element_by_xpath(
    '/html/body/main/article/section/form/div[1]/div[20]/div/div/fieldset/div/div/div[2]/div/label')
nxt_check_box.click()
time.sleep(.5)

# done
nxt_btn = driver.find_element_by_xpath('/html/body/main/article/section/form/div[2]/button')
nxt_btn.click()
time.sleep(.5)

nxt_btn = driver.find_element_by_xpath('/html/body/main/article/section/div[2]/a')
nxt_btn.click()
time.sleep(.5)

driver.quit()
