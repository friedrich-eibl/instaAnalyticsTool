#import json
from selenium import webdriver
from time import sleep
#import plotly.express as px

class InstaAnalytics:
    def __init__(self, usr):
        self.usr = usr
        self.following = 0
        self.followers = 0

        
        

    def grabData(self): 
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com/" + self.usr)

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
        self.followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")
        self.following = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text

ana = InstaAnalytics('friedricheibl')
ana.grabData()
print(ana.following, ana.followers)