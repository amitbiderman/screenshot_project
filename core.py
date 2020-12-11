import re
import shutil
from datetime import datetime
import time
import os.path
import validators
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from urllib3.exceptions import MaxRetryError


class WebSnapShooter:
    SCREENSHOOT_PATH = "/app/screenshot"

    def __init__(self):
        self.url_arg = None
        self.driver = None

    def format_url(self):
        # Add default URL protocol (HTTPS) if missing
        if not re.match('(?:[A-Za-z0-9-]+)://', self.url_arg):
            self.url_arg = 'https://{}'.format(self.url_arg)

    def validate_url(self):
        if self.url_arg is None:
            print("URL address doesn't exist!")
            return False

        self.format_url()

        if not validators.url(self.url_arg):
            print("Please enter a valid URL address!")
            return False

        return True

    def init_driver(self):
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        # Already initialized?
        if self.driver is not None:
            return True

        browser_options = Options()
        browser_options.add_argument("--headless")
        browser_options.add_argument("--no-sandbox")
        browser_options.add_argument("--disable-dev-shm-usage")
        browser_prefs = {"profile.default_content_settings": {"images": 2}}
        browser_options.experimental_options["prefs"] = browser_prefs

        try:
            self.driver = webdriver.Chrome(options=browser_options)
        except WebDriverException:
            print("Can't initialize web driver!")
            return False

        return True

    def open_url(self):
        # Check if Valid URL was provided
        try:
            self.driver.get(self.url_arg)
            self.driver.maximize_window()
        except (WebDriverException, MaxRetryError):
            self.driver.quit()
            print(f"Failed to open URL: {self.url_arg}")
            return False

        # Make sure the URL loaded
        time.sleep(1)
        return True

    def take_screenshot(self, url_arg):
        self.url_arg = url_arg

        if not self.validate_url():
            return False

        if not self.open_url():
            return False

        # Get current date and time in format: dd_mm_YYYY__H_M_S
        format = "%d_%m_%Y__%H_%M_%S"
        timestamp = datetime.now().strftime(format)

        if not os.path.exists(self.SCREENSHOOT_PATH):
            os.mkdir(self.SCREENSHOOT_PATH)

        picture = os.path.join(self.SCREENSHOOT_PATH, f"{timestamp}__screenshot.png")

        self.driver.get_screenshot_as_file(picture)

        # Validate creation of the picture
        return os.path.exists(picture) and os.stat(picture).st_size != 0

    def __del__(self):
        if self.driver is not None:
            self.driver.quit()
