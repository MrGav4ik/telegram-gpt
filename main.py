from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import google.generativeai as genai
import os
import time

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
telegram_password = os.getenv("TELEGRAM_PASSWORD")
user_id = os.getenv("USER_ID")

# Set up generative AI
genai.configure(api_key=gemini_api_key)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
model = genai.GenerativeModel("gemini-1.5-flash")

driver.get("https://web.telegram.org/k/")

# Wait until the input field for the password is visible and enabled
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "input-field-input"))
)

# Locate the password input field and ensure it's interactable
password = driver.find_element(By.CLASS_NAME, "input-field-input")

# Ensure the input field is enabled and interactable
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(password)
)

# Send password and press Enter
password.send_keys(telegram_password + Keys.ENTER)

# Wait for the user to be available
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", f'//a[@href="#{user_id}"]'))
)

# Click on the user
user = driver.find_element("xpath", f'//a[@href="#{user_id}"]')
user.click()

# Initialize a variable to store the last processed message text
last_data_mid = ""


# Begin the message-checking loop
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Assuming `driver` and `model` are initialized properly
last_data_mid = ""  # Initialize the last processed message's data-mid

try:
    while True:
        try:
            # Wait until the message bubbles are present and visible (up to 10 seconds)
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.bubble"))
            )

            # Get all message bubbles
            message_bubbles = driver.find_elements(By.CSS_SELECTOR, "div.bubble")

            if message_bubbles:
                # Get the 'data-mid' attribute of the latest message bubble
                latest_bubble = message_bubbles[-1]
                current_data_mid = latest_bubble.get_attribute("data-mid")

                # Check if this message is new by comparing data-mid values
                if current_data_mid != last_data_mid:
                    last_data_mid = current_data_mid  # Update last_data_mid with the latest
                    # Extract the latest message
                    try:
                        latest_message = latest_bubble.find_element(By.CSS_SELECTOR, "span.translatable-message").text
                        print("New message detected:", latest_message)

                        # Generate a new AI response
                        model_message = model.generate_content(latest_message).text
                        model_message_text = model_message.replace("\n", "")

                        # Send the new response to the chat
                        message_box = driver.find_element(By.CSS_SELECTOR, "div.input-message-input[contenteditable='true']")
                        message_box.click()
                        message_box.send_keys(model_message_text)
                        message_box.send_keys(Keys.ENTER)
                    except NoSuchElementException:
                        print("Error: Message text not found in the bubble.")
                        continue  # Skip this iteration and wait for the next one

        except Exception as check_error:
            print("Error while checking new messages:", check_error)

        # Sleep for a brief period (e.g., 1 second) to reduce CPU load and prevent rapid retries
        time.sleep(1)

except KeyboardInterrupt:
    print("Bot stopped manually.")

finally:
    driver.quit()  # Cleanup the browser window when exiting
