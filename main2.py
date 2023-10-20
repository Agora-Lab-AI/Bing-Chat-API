import os
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
from dotenv import load_dotenv

load_dotenv()

class BingChatAPI:
    def __init__(self, cookie_value: str):
        self.options = ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless")
        self.driver = Chrome(options=self.options)
        self.cookie_value = cookie_value
        self.limit_counter = 0  # Counter to manage chat rate limits

    def initialize(self):
        cookie = {"name": "_U", "value": self.cookie_value}
        self.driver.get("https://www.bing.com/chat")  # Replace with the actual Bing Chat URL
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def send_message(self, message: str):
        # Execute JavaScript to send a chat message
        js_script = f"""
        var chatBox = document.querySelector('your_chatbox_selector_here');
        chatBox.value = '{message}';
        chatBox.dispatchEvent(new Event('change'));
        """
        self.driver.execute_script(js_script)
        self.limit_counter += 1  # Increment the counter

    def get_latest_message(self):
        # Execute JavaScript to extract the latest chat message
        js_script = """
        var messages = document.querySelectorAll('your_message_selector_here');
        return messages[messages.length - 1].textContent;
        """
        try:
            return self.driver.execute_script(js_script)
        except Exception as e:
            logging.critical(f"Error while extracting chat messages: {e}")
            return None

    def get_text_completion(self, initial_text: str):
        if self.limit_counter >= 5:  # Reset chat after 5 messages
            self.initialize()
            self.limit_counter = 0

        self.send_message(initial_text)
        time.sleep(5)  # Wait for the chat service to respond; you can adjust this
        return self.get_latest_message()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    cookie_value = os.environ.get('BING_COOKIE', '')  # Read from environment variable

    if not cookie_value:
        logging.error("BING_COOKIE environment variable not set. Exiting.")
        exit(1)

    bing_chat_api = BingChatAPI(cookie_value)
    bing_chat_api.initialize()

    initial_text = "Once upon a time there was a cat named ______"
    completion = bing_chat_api.get_text_completion(initial_text)

    print(f"Initial text: {initial_text}\nCompletion: {completion}")
