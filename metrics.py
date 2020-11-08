#import json
from selenium import webdriver
from time import sleep
from datetime import datetime
#import plotly.express as px

class InstaAnalytics:
    def __init__(self, usr):
        self.usr = usr
        self.following = 0
        self.followers = 0

        self.data = []

        
        
    #opens Firefox and looks up follower count
    def grabData(self): 
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com/" + self.usr)

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
        self.followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")
        self.following = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text

        self.driver.quit()

ana = InstaAnalytics('friedricheibl')

#loop to check in one-hour intervals
while True:
    ana.grabData()
    timeNow = datetime.now()
    timestamp = timeNow.strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, "      Followers: ", ana.followers)
    ana.data.append((timestamp, ana.followers))
    sleep(3598) 
#print(ana.following, ana.followers)
print(ana.data)