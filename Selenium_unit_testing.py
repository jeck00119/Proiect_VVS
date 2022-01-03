# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebUnitTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        self.base_url = "http://127.0.0.1:5000/"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver = self.driver
        self.driver.get(self.base_url)

    def test_index_url(self):
        self.get_url = self.driver.current_url
        self.assertIn(self.base_url, self.get_url)

    def test_site1_link_exist(self):
        self.link_site1 = self.driver.find_element(By.LINK_TEXT, "Access first site")
        self.assertIn("Access first site", self.link_site1.text)

    def test_site1_link_click(self):
        self.link_site1 = self.driver.find_element(By.LINK_TEXT, "Access first site")
        self.link_site1.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:5000/site1", self.get_url)

    def test_page1_FirstName_input(self):
        self.link_site1 = self.driver.find_element(By.LINK_TEXT, "Access first site")
        self.link_site1.click()
        self.link_site1 = self.driver.find_element(By.ID, "fname")
        self.link_site1.send_keys("test first")
        first_name = self.link_site1.get_attribute('value')
        self.assertIn("test first", first_name)

    def test_page1_LastName_input(self):
        self.link_site1 = self.driver.find_element(By.LINK_TEXT, "Access first site")
        self.link_site1.click()
        self.link_site1 = self.driver.find_element(By.ID, "lname")
        self.link_site1.send_keys("test last")
        last_name = self.link_site1.get_attribute('value')
        self.assertIn("test last", last_name)

    def test_page1_submitButton_exist(self):
        self.link_site1 = self.driver.find_element(By.LINK_TEXT, "Access first site")
        self.link_site1.click()
        btn_name = self.driver.find_element(By.ID, "btn")
        self.assertIn("Submit", btn_name.text)

    def test_site2_link_exist(self):
        self.link_site2 = self.driver.find_element(By.LINK_TEXT, "Access second site")
        self.assertIn("Access second site", self.link_site2.text)

    def test_site2_link_click(self):
        self.link_site2 = self.driver.find_element(By.LINK_TEXT, "Access second site")
        self.link_site2.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:5000/site2", self.get_url)

    def test_page2_textColorChange_click(self):
        self.link_site2 = self.driver.find_element(By.LINK_TEXT, "Access second site")
        self.link_site2.click()
        self.link_site2 = self.driver.find_element(By.ID, "myId")
        self.link_site2.click()
        text_color = self.link_site2.value_of_css_property("color")
        self.assertIn("rgb(0, 128, 0)", text_color)  # green

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
