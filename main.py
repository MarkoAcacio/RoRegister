import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random as rd
import time


characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']
username = ""
password = ""

choice = input("\nChoose an Account Creation Method: \n\nType 1 : Username & Password of your choice. \nType 2 : Random Username & Password ( will be provided after sign up )\n\n")

def userGen(usrLngth):
    usrgen = ''.join(rd.sample(characters,int(usrLngth)))
    return usrgen

def userPas(usrPLngth):
    usrpass = ''.join(rd.sample(characters,int(usrPLngth)))
    return usrpass

def Register(usr, passw):

    path = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=path) 
    print("\n\nConnected to Roblox")
    driver.get("https://www.roblox.com/")

    selectMonth = driver.find_element(By.NAME, 'birthdayMonth')
    selectDay = driver.find_element(By.NAME, 'birthdayDay')
    selectYear = driver.find_element(By.NAME, 'birthdayYear')

    time.sleep(0.5)
    select = Select(selectMonth)
    select.select_by_value('Mar')

    time.sleep(0.5)
    select = Select(selectDay)
    select.select_by_value('10')    
    
    time.sleep(0.5)
    select = Select(selectYear)
    select.select_by_value('2005')

    time.sleep(0.5)
    driver.find_element(By.NAME, 'signupUsername').send_keys(usr)
    time.sleep(0.5)
    driver.find_element(By.NAME, 'signupPassword').send_keys(passw)
    time.sleep(0.5)
    driver.find_element(By.ID, 'MaleButton').click()
    time.sleep(0.5)
    driver.find_element(By.ID, 'signup-button').click()

    time.sleep(25)



if int(choice) == 1:
    username = input("\n\nEnter Username\n")
    password = input("Enter Password\n")
    

elif int(choice) == 2:
   print("\n\nUsername Length can only be 3-20 characters long. \nPassword must be between 8 and 200 characters long. \n")
   usrlength = input("Enter The Length of the Username: ")
   usrpasslength = input("Enter The Length of the Password: ")

   generatedUsername = userGen(usrlength)
   generatedPassword = userPas(usrpasslength)

   print(f"\nUsername: {generatedUsername}\nPassword: {generatedPassword}")

   Register(generatedUsername, generatedPassword)


else:
    print("Invalid Choice.")