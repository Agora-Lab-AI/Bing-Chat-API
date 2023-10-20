<<<<<<< HEAD
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
=======
import os
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
from dotenv import load_dotenv

>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
load_dotenv()

class BingChatAPI:
    def __init__(self, cookie_value: str):
        self.options = ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
<<<<<<< HEAD
        # Conditionally remove the --headless option
        if "--headless" in self.options.arguments:
            self.options.arguments.remove("--headless")

        self.driver = Chrome(options=self.options)
        self.cookie_value = cookie_value  # Make sure this line is executed

    def initialize(self):
        cookie = {"name": "_U", "value": self.cookie_value}
        self.driver.get("https://www.bing.com/search?q=Bing+AI&showconv=1")
=======
        self.options.add_argument("--headless")
        self.driver = Chrome(options=self.options)
        self.cookie_value = cookie_value
        self.limit_counter = 0  # Counter to manage chat rate limits

    def initialize(self):
        cookie = {"name": "_U", "value": self.cookie_value}
        self.driver.get("https://www.bing.com/chat")  # Replace with the actual Bing Chat URL
>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    def send_message(self, message: str):
<<<<<<< HEAD
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
=======
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
>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
        except Exception as e:
            logging.critical(f"Error while extracting chat messages: {e}")
            return None

    def get_text_completion(self, initial_text: str):
<<<<<<< HEAD
        self.initialize()
        self.send_message(initial_text)
=======
        if self.limit_counter >= 5:  # Reset chat after 5 messages
            self.initialize()
            self.limit_counter = 0

        self.send_message(initial_text)
        time.sleep(5)  # Wait for the chat service to respond; you can adjust this
>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
        return self.get_latest_message()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

<<<<<<< HEAD
    # Make sure you've set the environment variable BING_COOKIE
    cookie_value = os.environ.get('BING_COOKIE', '')
=======
    cookie_value = os.environ.get('BING_COOKIE', '')  # Read from environment variable

>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
    if not cookie_value:
        logging.error("BING_COOKIE environment variable not set. Exiting.")
        exit(1)

    bing_chat_api = BingChatAPI(cookie_value)
<<<<<<< HEAD
    initial_text = "Once upon a time there was a cat named ______"
    completion = bing_chat_api.get_text_completion(initial_text)
=======
    bing_chat_api.initialize()

    initial_text = "Once upon a time there was a cat named ______"
    completion = bing_chat_api.get_text_completion(initial_text)

>>>>>>> f8aec2dd57551ae4ae1d19f300f902cbbeb95d2a
    print(f"Initial text: {initial_text}\nCompletion: {completion}")
