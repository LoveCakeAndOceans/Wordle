from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
import function_Wordle
import read_Site

if len(sys.argv) > 1:
    site = sys.argv[1]

else:
    site = "nyt"

    
#Creates the driver we need to interact with chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #Deprecation Warning. 


#Below we open up the website we need, either NYT or wordlegame

# =============================================================================
# New York Times
# =============================================================================
if site == "nyt":
    driver.get("https://www.nytimes.com/games/wordle/index.html") #Opens Page
    
    driver.find_element(By.ID, "pz-gdpr-btn-accept").click() #Accepts Cookies
    
    close = ActionChains(driver) #Closes Instructions Box
    close.send_keys(Keys.ENTER)
    close.pause(1.5)
    close.perform()

# =============================================================================
# Other Website
# =============================================================================
else:
    driver.get("https://wordlegame.org?challenge=Y292ZXI")
    time.sleep(5)





#Creates an Action Chain object that we will be using the input the newest word
actions = ActionChains(driver)


#characters will be used to tell the read_Site module what letters don't need to be sent back after reading the keyboard
characters = ""
#We use a try statement and a finally so we will make sure to close the browser when we are done. 
try:
    for i in range(6):
        x = function_Wordle.new[0]      #Gets the first word in list of words ordered by score
        actions.send_keys(x)            #The next few lines outline and perform the actions to enter the word
        actions.send_keys(Keys.ENTER)
        
        if site == "nyt":
            actions.pause(2)
        else:
            actions.pause(5)
            
        actions.perform()
        
        
        
        conditions, complete = read_Site.get_conditions(driver,characters, site) #conditions will be a list of lists with 2 entries each ()
        if complete:                            #Breaks out of the loop when the program has been solved
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
                
        if function_Wordle.a_return(a, c, p) == "Empty": #If after ordering the list, we run out of words we break out of the loop. Otherwise we go back up and set x to the newest first option in the list
                print("The program is out of words and will end.")
                break
        
    
        
    time.sleep(2)
    driver.quit()
    
finally:
    
    driver.quit()
    
   




#AUTOGUI
# import pyautogui
# pyautogui.leftClick()
# j = 1
# while True:
#     for i in "arose":    
#         pyautogui.write(i)
#         time.sleep(0.1)
#     pyautogui.press('enter')