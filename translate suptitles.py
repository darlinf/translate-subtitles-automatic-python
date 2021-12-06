from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re

def removeArrow():
    file = open("suptitles/1 Suptitle.txt", "r") 
    splitText = re.split("\n", file.read().replace("<", "b"))
    splitText.pop(1)
    resultSuptitle = ""  
    timeLine = []

    j = 0
    for i in splitText:
        if "-->" in i:
            splitText.pop(j - 1)
        j += 1
            
    for i in splitText:
        if "-->" not in i and "WEBVTT" not in i: 
            resultSuptitle += i + '\n' 
        elif i not in "WEBVTT": 
            timeLine.append(i) 

    file = open("suptitles/2 English.txt", "a")
    file.write(resultSuptitle)
    file.close() 

    return timeLine


def trasnlate():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://translate.google.com/?op=docs") 

    driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[1]/c-wiz/div[5]/div/div[2]/div/div/span/button[2]").click()

    upload_file = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/div/form/div[1]/div[3]/input")
    upload_file.send_keys("C:/Users/DarlinFabianLeyba/Desktop/suptitles processing/suptitles/2 English.txt")

    driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[3]/c-wiz/div[2]/c-wiz/div/div/form/div[2]/div[2]/div/button").click()
    
    return driver.find_element_by_xpath("/html/body/pre").text.split("\n")
    
   
def unionString(timeLine, splitTextSpanish):
    
    file = open("suptitles/2 English.txt", "r")
    splitTextEnglish = re.split("\n", file.read())

    unionResult = "WEBVTT \n \n" + timeLine[0] + "\n"

    j = 0
    jT = 1
    for i in splitTextEnglish:
        if i != "" and j < len(splitTextSpanish):
            unionResult += i + "\n" + splitTextSpanish[j]+ "\n"
        elif jT < len(timeLine):
            unionResult += "\n" + timeLine[jT] + "\n"
            jT += 1
        j += 1 

    file = open("suptitles/4 Suptitle result.txt", "a", encoding="utf-8")
    file.write(str(unionResult))
    file.close() 


timeLine = removeArrow()
textSpanish = trasnlate()
unionString(timeLine, textSpanish)

