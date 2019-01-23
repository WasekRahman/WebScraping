

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os


def dhl(tracking):
    chrome_driver = "C:\\Users\\Dell\\Desktop\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)

    target = 'http://www.dhl.com.bd/en/express/tracking.html?AWB={}&brand=DHL'.format(tracking)
    driver.get(target)

    soup = BeautifulSoup(driver.page_source, "lxml")
    tables = soup.find("div",{"class":"tracking-result express"})
    table = tables.findAll(['thead','tbody'])
    head = []
    for t in table:
        texts = t.findAll('tr')
        for text in texts:
            try:
                var = ' '.join(text.text.split())
            except:
                var = ''
            head.append(var)
    return convert(head)

def convert(head):
    df = pd.DataFrame()
    df['Update']=head
    return df


def savedata(tracking,data):
    filename = '{}.csv'.format(tracking)
    checkname = os.path.exists(filename)
    if not checkname:
        data.to_csv(filename, index=False)
        print("Saved")
    else:
        replace = input("FILE ALREADY EXISTS. REPLACE FILE? Y/N: ")
        if(replace=='Y'):
            os.remove(filename)
            data.to_csv(filename, index=False)
            print("Updated")
        else:
            print("")

tracking = input('Enter the 10 digit tracking number: ')
if(len(tracking)==10):
    data = dhl(tracking)
    print(data)
else:
    print("Invalid tracking!")
save = input('Do you want to save data? Y/N: ')
if(save == 'Y'):
    savedata(tracking,data)
else:
    print("Completed")
