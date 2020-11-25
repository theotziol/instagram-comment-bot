''' By theotziol
install libraries με pip install 
κάνε download webdriver ανάλογα τι έχεις, εγώ έχω chrome (πρέπει να έχει ίδια έκδοση)'''
from selenium import webdriver as wd
from psw import psw,name #ekana diaforetiko arxeio me onoma psw gia na valw apo ekei tous kwdikous na mhn fainontai sto story
import time
from random import randint as rndm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
site = 'https://instagram.com'
post = 'https://www.instagram.com/p/CH-MgQOn-7E/'

class bot:
    def __init__(self, site, psw, name):
        self.driver = wd.Chrome()
        time.sleep(2)
        self.driver.get(site)
        self.name = name
        self.psw = psw
        self.wait = WebDriverWait(self.driver, 10)

    def enter(self):
        path_cookies = '/html/body/div[2]/div/div/div/div[2]/button[1]'
        path_login = '//*[@id="loginForm"]/div/div[3]/button'
        path_not_now = '//*[@id="react-root"]/section/main/div/div/div/div/button'
        path_notifications = '/html/body/div[4]/div/div/div/div[3]/button[2]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, path_cookies))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME ,'username'))).send_keys(self.name)
        self.wait.until(EC.presence_of_element_located((By.NAME ,'password'))).send_keys(self.psw)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, path_login))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH ,path_not_now))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH ,path_notifications))).click()

    def search(self, name = 'alexandros_kopsialis'):
        search_path = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div'
        search_name = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        name_select = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]'
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH ,search_path))).click()
        #self.wait.until(EC.presence_of_element_located((By.XPATH ,search_name))).send_keys(name)
        #self.wait.until(EC.element_to_be_clickable((By.XPATH ,name_select))).click()
        self.driver.get(post)
        
    def comment(self):
        path_to_comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button'
        path_to_keys = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
        path_to_submit = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button'
        while True:
            friends = []
            for i in self.text():
                friends.append(i)
            print(friends)
            self.wait.until(EC.element_to_be_clickable((By.XPATH ,path_to_comment))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH ,path_to_keys))).send_keys(friends[3] + ' ' + friends[0] + ' ' + friends[1] + ' '+ friends[2] + ' ')
            self.wait.until(EC.element_to_be_clickable((By.XPATH ,path_to_submit))).click()
            del friends[:]
            time.sleep(200) #βάλε χρόνο σε sec time for comment
        
    def text(self):
        friends = ['@example_tag_name','@','@', '@',
                   '@', '@', '@']#δήλωσε άτομα που θα τους τα κάνεις μπάλες @tag names
        text = ['nai re', 'pame', 'ok', 'one more', 'yeah', 'cool',
                'winner winner chicken dinner','omg','joey doesnt share food'] #γραφω χαζομάρες να μην ειναι μόνο ταγκ (some text)
        friend_to_comment = []
        while True:
            num = rndm(0, len(friends)-1)
            if friends[num] not in friend_to_comment:
                friend_to_comment.append(friends[num])
                if len(friend_to_comment) == 3:
                    break
        text_num = rndm(0, len(text)-1)
        friend_to_comment.append(text[text_num])
        for item in friend_to_comment:
            yield item
                       
        
test = bot(site, psw, name) #δήλωσε δικούς σου κωδικούς
test.enter()
test.search()
test.comment()
