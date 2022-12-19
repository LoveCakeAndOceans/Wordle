from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



    
email = "bifola1313@nazyno.com"
password = 'awdthilp135"$^'

#Creates the driver we need to interact with chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #Deprecation Warning. 

driver.get("https://myaccount.nytimes.com/auth/enter-email?response_type=cookie&client_id=games&application=nyt-lires&redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fgames%2Fwordle%2Findex.html")

for i in range(2):
    #Email
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "email").send_keys(Keys.ENTER)
    
    #Password
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    test = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password")))
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(password, Keys.ENTER)
    
    #Break since we won't need to do a captcha a second time
    if i == 1:
        break
    
    #Clicking the Captcha box
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border")))
    driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
    driver.switch_to.parent_frame()



import function_Wordle
import read_Site
site = "nyt"
actions = ActionChains(driver)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div > div > dialog > div > button > svg"))) #CLASS_NAME, "Modal-module_paddingTop__c-KJb")))
element.click()
# actions.send_keys(Keys.ENTER)
# actions.pause(1.5)
# actions.perform()


characters = ""
try:
    for i in range(6):
        x = function_Wordle.new[0]
        actions.send_keys(x)            
        actions.send_keys(Keys.ENTER)
        actions.pause(2)
        actions.perform()
        print(x, i)
        
        conditions, complete = read_Site.get_conditions(driver,characters, site) 
        if complete:                            
            print("The answer has been found!")
            break
        
        a = ""
        c = []
        p = []
        for i in conditions:
            if i[1] == "absent":
                a = a + i[0]
                characters = characters + i[0]
                
            elif i[1] == "correct":
                c.append([i[0], x.find(i[0])])
                characters = characters + i[0]
                
            elif i[1] == "present":
                p.append([i[0], x.find(i[0])])
                
            else:
                
                print("There is a problem here.", i)
                exit()
                
        if function_Wordle.a_return(a, c, p) == "Empty":
                print("The program is out of words and will end.")
                break
        
    
        
    time.sleep(8)
    driver.quit()

finally:
    driver.quit()

    
    
    
    
    
    