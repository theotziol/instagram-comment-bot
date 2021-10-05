#update 5/10/2021


from selenium import webdriver as wd

from selenium.webdriver.support.ui import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from random import randint

from usern import username, password #έκανα εισαγωγή το password και το username Για να μην φανεί στο video


site = 'https://instagram.com'

path_cookies = '/html/body/div[4]/div/div/button[1]'
path_username = '//*[@id="loginForm"]/div/div[1]/div/label/input'
path_password = '//*[@id="loginForm"]/div/div[2]/div/label/input'
path_submit = '//*[@id="loginForm"]/div/div[3]/button'
path_cookies2 = '/html/body/div[4]/div/div/button[2]'
path_notnow = '//*[@id="react-root"]/section/main/div/div/div/div/button'
path_noti = '/html/body/div[5]/div/div/div/div[3]/button[2]'

post = 'https://www.instagram.com/p/CQooh-eH440/'

path_to_comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button/div'
path_comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/div/div/section[3]/div/form/textarea'
path_post = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]'
id_textarea = 'Ypffh'
class_post = 'sqdOP yWX7d    y3zKF     '
driver = wd.Chrome()
driver.get(site)



driver.find_element_by_xpath(path_cookies).click()
time.sleep(2)
driver.find_element_by_xpath(path_username).send_keys(username)
driver.find_element_by_xpath(path_password).send_keys(password)
wait = ww(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH,path_submit))).click()
time.sleep(2)
#driver.find_element_by_xpath(path_submit).click()

#Πιθανον να χρειαστεί και αυτό το path

#wait.until(EC.element_to_be_clickable((By.XPATH,path_cookies2))).click() 
wait.until(EC.element_to_be_clickable((By.XPATH,path_notnow))).click()
time.sleep(1)
#driver.find_element_by_xpath(path_notnow).click()
wait.until(EC.element_to_be_clickable((By.XPATH,path_noti))).click()
time.sleep(1)
#driver.find_element_by_xpath(path_noti).click()
driver.get(post)


friends = ['@theotziol' , '@theotziolphotography', 'allotag', 'αλλλοταγκ2', 'ο τζιολας ειναι υπεροχος' ,'κανε σαμπσκραιμπ']




t = 0
while t < 10:
    random_list = []

    for i in range(100):
        random = randint(0, len(friends)-1)
        if random not in random_list:
            random_list.append(random)
        if len(random_list) == 3:
            break
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH,path_to_comment))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME ,id_textarea))).send_keys(friends[random_list[0]] + ' ' + friends[random_list[1]] + ' ' + friends[random_list[2]] + ' ' )
    #wait.until(EC.element_to_be_clickable((By.CLASS_NAME,class_post))).click()
    time.sleep(3)
    t = t + 1
    del random_list




