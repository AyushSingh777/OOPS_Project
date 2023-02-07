from selenium import webdriver
from selenium.webdriver.common.by import By



class InstagramLogin(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Log in')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()


class InstagramVerify(InstagramLogin):
    def verify_login(self):
        expected = self.driver.find_element(By.XPATH, "//a[contains(text(),'honeypratap')]").text
        print(expected)

    def ele(self):
        try:
            self.driver.find_element(By.NAME,"username").click()
        except:
            print("Invalid xpath")

if __name__ == '__main__':

    while True:
        print("Enter 1 for login")
        print("Enter 2 for login verify")
        print("Enter 3 for check")
        print("Enter 4 to exit")
        userchoice = int(input())
        if userchoice == 1:
            login = InstagramVerify('honeypratap', 'Gujjar@77')
            login.login()
        elif userchoice ==2:
            login.verify_login()
        elif userchoice == 3:
            login.ele()
        elif userchoice == 4:
            quit()






