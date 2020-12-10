import re
from selenium import webdriver
from selenium.webdriver import Firefox
import time
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import MaxRetryError
import os.path
import validators
from selenium.webdriver.chrome.options import Options


class Screenshot:

    def __init__(self, url_arg):
        self.url_arg = url_arg
        self.driver = None
        self.chrome_options = None

    def user_input(self):
        if self.url_arg is None:
            exit(print("Please enter a valid URL address!"))

        self.format_url()

        if not validators.url(self.url_arg):
            exit(print("Please enter a valid URL address!"))
        else:
            self.open_url()

    def set_chrome_options(self):
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        self.chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}

        self.driver = webdriver.Chrome(options=self.chrome_options)


    def format_url(self):
        # Adding proper URL characters if missing
        if not re.match('(?:http|ftp|https)://', self.url_arg):
            self.url_arg = 'https://{}'.format(self.url_arg)

    def open_url(self):
        # Check if Valid URL was provided
        try:
            self.driver.get(self.url_arg)
            self.driver.maximize_window()
        except (WebDriverException, MaxRetryError):
            self.driver.quit()
            exit(print("Please enter a valid URL address!"))

    def take_screenshot(self):
        number = 1
        time.sleep(1)

        while True:
            picture = f"screenshot{number}.png"
            if not os.path.exists(picture):
                self.driver.get_screenshot_as_file(picture)
                break
            else:
                number += 1

        if os.path.exists(picture) and os.stat(picture).st_size != 0:
            self.driver.quit()
        else:
            self.take_screenshot()
