from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

class BingChatAPI:
    def __init__(self, cookie_value: str):
        self.options = ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # Conditionally remove the --headless option
        if "--headless" in self.options.arguments:
            self.options.arguments.remove("--headless")

        self.driver = Chrome(options=self.options)
        self.cookie_value = cookie_value  # Make sure this line is executed

    def initialize(self):
        cookie = {"name": "_U", "value": self.cookie_value}
        self.driver.get("https://www.bing.com/search?q=Bing+AI&showconv=1")
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def send_message(self, message: str):
        chat_box = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.ID, "searchbox"))
        )
        chat_box.send_keys(message)
        chat_box.send_keys(Keys.RETURN)

    def get_latest_message(self):
        try:
            messages = WebDriverWait(self.driver, 60).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "ac-textBlock"))
            )
            return messages[-1].text if messages else None
        except Exception as e:
            logging.critical(f"Error while extracting chat messages: {e}")
            return None

    def get_text_completion(self, initial_text: str):
        self.initialize()
        self.send_message(initial_text)
        return self.get_latest_message()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Make sure you've set the environment variable BING_COOKIE
    cookie_value = os.environ.get('BING_COOKIE', '')
    if not cookie_value:
        logging.error("BING_COOKIE environment variable not set. Exiting.")
        exit(1)

    bing_chat_api = BingChatAPI(cookie_value)
    initial_text = "Once upon a time there was a cat named ______"
    completion = bing_chat_api.get_text_completion(initial_text)
    print(f"Initial text: {initial_text}\nCompletion: {completion}")
