from selenium.webdriver.common.by import By


def get_conditions(driver, letters_done = "", site = "nyt"):
    
    l = []
    
    #NYT code
    if site == "nyt":
        #Below we find the keyboard element. We make a list of all the row elements
        #We then make a list of all the button elements in a row. And create a list
        #of each button's "accessible_name". We do this for each row. Finally we remove the "ENTER" and "backspace" keys.
        board = driver.find_element(By.CLASS_NAME, "Keyboard-module_keyboard__1HSnn")
        
        rows = board.find_elements(By.CLASS_NAME, "Keyboard-module_row__YWe5w")
        for row in rows:
            buttons = row.find_elements(By.CLASS_NAME, "Key-module_key__Rv-Vp")
        
            for button in buttons:
                #print(button.accessible_name)
                l.append(button.accessible_name)
                #print(button.text)
        l.remove("ENTER")
        l.remove("backspace")
        
        
        listy = [y.lower() for y in l] 
        
        l = []
        for i in listy:             
            l.append(i.split(" "))
            
        for i in l[:]:              
            if len(i) == 1:
                l.remove(i)
    
    
    
    
    
    if site == "game":
        board = driver.find_element(By.CLASS_NAME, "Game-keyboard")
        rows = board.find_elements(By.CLASS_NAME, "Game-keyboard-row")
        for row in rows:
            
            absent_buttons = row.find_elements(By.CLASS_NAME, "letter-absent")
            for button in absent_buttons:
                l.append(button.text + " absent")
            
            elsewhere_buttons = row.find_elements(By.CLASS_NAME, "letter-elsewhere")
            for button in elsewhere_buttons:
                l.append(button.text + " present")
            
            correct_buttons = row.find_elements(By.CLASS_NAME, "letter-correct")
            for button in correct_buttons:
                l.append(button.text + " correct")
            
            
        listy = [y.lower() for y in l] #Lowering every character in each "accessible_name" string.
        
        l = []
        for i in listy:             #Turning each string into a list where the items are split if there is a space
            l.append(i.split(" "))
            
        
        
    
                
                
                
    finished = 0
    for i in l:                 #We check if there are five correct letters on the keyboard, indicating the game has been won
        if i[1] == "correct":
            finished = finished + 1
    
    for i in letters_done:      #We remove any letters from the list if we have already modified our list, so we aren't modifying it again needlessly (excluding orange letters as they may need to be modified multiple times)
        for j in l[:]:
            if i in j[0]:
                l.remove(j)
                
    #We return the list and whether the game has been solved.
    if finished == 5:
        return l, True
    else:
        return l, False


    
    
    
    
    