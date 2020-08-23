import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******************** Test_001_Login **********")
        self.logger.info("****** verifying home page title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test is passed ************")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.logger.info("**** Home page title test is failed ************")
            assert False
        self.driver.close()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("******************** Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickUserLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******************** Login Test is passed **********")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_Login.png")
            self.logger.error("******************** Login Test is failed **********")
            assert False
        self.driver.close()
