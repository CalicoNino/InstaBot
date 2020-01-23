from selenium import webdriver
import time


class InstaBot:
    def __init__(self, username, password):
        super().__init__()

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("chromedriver.exe")
        time.sleep(2)
        
        
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        userElem = self.driver.find_element_by_xpath("//input[@name='username']")
        userElem.clear()
        userElem.send_keys(self.username)

        passElem = self.driver.find_element_by_xpath("//input[@name='password']")
        passElem.clear()
        passElem.send_keys(self.password)

        loginBut = self.driver.find_element_by_xpath("//button[@type='submit']")
        loginBut.click()

        time.sleep(4)

        skipBut = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        skipBut.click()

        time.sleep(2)

    def search(self, username):
        self.driver.get("https://www.instagram.com/" + username)
        time.sleep(3)
        
    def unfollow(self, username):
        self.search(username)
        unfollowBut = self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]")
        unfollowBut.click()
        time.sleep(1)
        unfollowBut_check = self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")
        unfollowBut_check.click()
        time.sleep(3)

    def follow(self, username):
        self.search(username)
        followBut = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        followBut.click()
        time.sleep(3)

    def follow_userfollowers(self, username):
        self.search(username)
        followersBut = self.driver.find_element_by_xpath("//a[contains(@href,'{0}/followers')]".format(username))
        followersBut.click()
        time.sleep(3)

    def follow_userfollowing(self, username):
        self.search(username)
        followBut = self.driver.find_element_by_xpath("//button[contains(text(), 'following')]")
        followBut.click()
        time.sleep(3)

        
        
        
        
        

        

        


        
        

    
        
        

