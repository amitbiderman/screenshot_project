from core import Screenshot
import sys
import os


class Main:
    def __init__(self):
        self.url_arg = sys.argv[1]
        self.screenshot = None

    def main(self):
        self.screenshot = Screenshot(self.url_arg)
        while True:
            self.screenshot.set_chrome_options()
            self.screenshot.user_input()
            self.screenshot.take_screenshot()
            break


if __name__ == '__main__':
    main = Main()
    main.main()
