import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class InstagramLogin(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

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
        return expected

    def element(self):
        try:
            self.driver.find_element(By.NAME,"username").click()
        except:
            return "Invalid xpath"

@pytest.fixture(scope="module")
def setup_module(request):
    login = InstagramVerify('honeypratap', 'Gujjar@77')
    login.login()
    def teardown_module():
        login.driver.close()
    request.addfinalizer(teardown_module)
    return login

def test_verify_login(setup_module):
    expected = setup_module.verify_login()
    assert expected == "honeypratap", f"Expected {expected} to be honeypratap"

def test_element(setup_module):
    expected = setup_module.element()
    assert expected == "Invalid xpath", f"Expected {expected} to be Invalid xpath"
