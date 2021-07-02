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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date, datetime

site = 'https://instagram.com'
post = 'https://www.instagram.com/p/COaPgOAnYZw/'
#post1 = 'https://www.instagram.com/p/CJDzUzTHzXy/'

c_time = datetime.now()
c_day = date.today()
day = c_day.strftime("%B_%d_%Y")

class bot:
    def __init__(self, site, psw, name):
        self.driver = wd.Chrome()
        time.sleep(2)
        self.driver.get(site)
        self.name = name
        self.psw = psw
        self.wait = WebDriverWait(self.driver, 15)

    def enter(self):
        path_cookies = '//button[text()="Accept All"]'
        path_login = '//*[@id="loginForm"]/div/div[3]/button'
        path_not_now = '//*[@id="react-root"]/section/main/div/div/div/div/button'
        path_notifications = '/html/body/div[4]/div/div/div/div[3]/button[2]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, path_cookies))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME ,'username'))).send_keys(self.name)
        self.wait.until(EC.presence_of_element_located((By.NAME ,'password'))).send_keys(self.psw)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, path_login))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH ,path_not_now))).click()
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH ,path_notifications))).click()
        except:
            pass

    def search(self, x):

        if x:
            self.driver.get(post)
            time.sleep(3)
        else: self.driver.get(post1)
        
    def comment(self):
        path_to_comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button'
        path_to_keys = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
        
        path_to_submit = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/button[2]' #'//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button'
        
        failed_attempts = 0
        comments = 0
        x = True
        while True:
            
            friends = []
            for i in self.text():
                friends.append(i)
            print(friends)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH ,path_to_comment))).click()
                time.sleep(3)
                if x:
                    
                    self.wait.until(EC.presence_of_element_located((By.XPATH ,path_to_keys))).send_keys(friends[1] + ' '+ friends[2] + ' '+ friends[0] + ' ')#(' ' + friends[3] + ' ' + friends[1] + ' '+ friends[2] + ' '+ friends[0] + ' ')
                    time.sleep(2)
                else: self.wait.until(EC.presence_of_element_located((By.XPATH ,path_to_keys))).send_keys(' ' + friends[1] + ' '+ friends[2] + ' ')
                time.sleep(1)
                self.driver.find_element_by_xpath(path_to_submit).click()
                time.sleep(3)
                self.driver.find_element_by_xpath(path_to_comment)
                comments += 1
                print("Comments commited = {}".format(comments))
            except:
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0, 300)")
                #if failed_attempts == 0 or failed_attempts % 2 == 0:
                    #x = not x
                    #self.search(x)
                #else: self.driver.refresh()
                self.driver.refresh()
                time.sleep(3)
                failed_attempts +=1
                if failed_attempts == 10 or failed_attempts == 14 or failed_attempts == 25 or failed_attempts == 35:
                    self.driver.execute_script("window.scrollTo(0, 300)")
                    self.driver.execute_script("window.scrollTo(0, 100)")
                    time.sleep(100)
                    self.driver.execute_script("window.scrollTo(0, 300)")
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, 100)")
                    time.sleep(1)
                print("failed attempts = {}".format(failed_attempts))
                time.sleep(8) 
                if failed_attempts == 30:
                    self.delete_cache()
                    self.driver.close()
                    break
            del friends[:]
            time.sleep(3) #βάλε χρόνο σε sec
        return comments - failed_attempts
    def text(self):
        friends = ['@','@','@kleopats', '@','@', '@','@',
                   '@', '@', '@','@', 
                   '@','@georfouk1','@','@','@','@','@']#δήλωσε άτομα που θα τους τα κάνεις μπάλες
        text = ['nai re', 'pame', 'ok', 'one more', 'yeah', 'cool',
                'τελειο δωρο','omg','καταπληκτικό', 'makari','το θέλω','τέλειο', 'φανταστικό','sorry για τα ταγκς',
                'θα βλεπετε το ονομα μου ολη μερα','θα σας τα κανω τσουρεκια','τα θέλω όλα','μην με κανετε μπλογκ plz','καλό πολύ καλό','αιντε μωρέ','νιωθω θετικά', 'εχω θετική αυρα',
                'τα vibes μου είναι θετικότατα', 'pame na kerdisoume','for the win', 'δωραρες','δεν ξερω τι να πω','τι διαγωνισμός ειναι αυτός ρε μλκ','','αίντε να κάνουμε καλοκαίρι','an kerdisw kernaw',
                'πω πω πω', 'Ompo mpo','sok', 'διαγωνισμός σοκ'] #γραφω χαζομάρες να μην ειναι μόνο ταγκ
        friend_to_comment = []
        while True:
            num = rndm(0, len(friends)-1)
            if friends[num] not in friend_to_comment:
                friend_to_comment.append(friends[num])
                if len(friend_to_comment) == 3:
                    break
        text_num = rndm(0, len(text)-1)
        #friend_to_comment.append(text[text_num]) text #δεν χρησιμοποιώ τις χαζομ΄ρες που έγραψα και χρησιμοποιώ μόνο τα τάγκ
        for item in friend_to_comment:
            yield item
    
    def delete_cache(self):
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        self.driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
        time.sleep(2)
        actions = ActionChains(self.driver) 
        actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
        actions.perform()
        time.sleep(2)
        actions = ActionChains(self.driver) 
        actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
        actions.perform()
        time.sleep(5) # wait some time to finish
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close() # close this tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        #self.driver.get(self.site)# switch back
commited = []

while True:        
    test = bot(site, psw, name) #δήλωσε δικούς σου κωδικούς
    test.enter()
    test.search(True)
    n = test.comment()
    f = open('{}.txt'.format(day),'a')
    print('comments in this round = {}'.format(n))
    f.write("Comments in this round = {}".format(n))
    f.write("\n")
    f.close()
    commited.append(n)
    if n <= 4:
        break
print(commited)
num = 0
for i in range(len(commited)):
    num += commited[i]
f = open('{}.txt'.format(day),'a')
f.write("Comments commited today {}".format(num))
f.close()
