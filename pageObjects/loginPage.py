from selenium import webdriver

class Login:

    def __init__(self, driver):
        self.driver = driver

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_css = "input[value='Log in']"

    link_logOut_linkText = "Logout"

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickUserLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()

    def clickLogOut(self):
        self.driver.find_element_by_link_text(self.link_logOut_linkText).click()
