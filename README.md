
# Telegram Chatbot with AI Integration

This project uses Selenium WebDriver to interact with Telegram Web, combined with Google's generative AI API (Gemini), to automatically respond to messages from a specific user. The bot listens for incoming messages and generates responses using an AI model, then sends those responses back to the chat.

## Features

- **Automated Login**: Logs into Telegram Web using credentials stored in environment variables.
- **Message Monitoring**: Monitors messages from a specific user and responds to them automatically.
- **AI Response Generation**: Uses Google's Gemini API (Generative AI) to create relevant responses to incoming messages.
- **Selenium WebDriver Automation**: Utilizes Selenium for browser automation to interact with Telegram Web.

## Requirements

- **Python 3.x**
- **Selenium**: For browser automation.
- **Google Generative AI**: For AI-powered responses.
- **dotenv**: To manage environment variables.
- **Chromedriver**: To run the Selenium WebDriver with Chrome.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/telegram-chatbot.git
   cd telegram-chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of the project.
   - Add the following variables to the `.env` file:
     ```env
     GEMINI_API_KEY=your_api_key
     TELEGRAM_PASSWORD=your_telegram_password
     USER_ID=your_user_id
     ```

5. **Download and install ChromeDriver**:
   - Download ChromeDriver compatible with your version of Chrome: [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Place `chromedriver.exe` in the project directory or update the path in the script.

## Usage

1. **Run the bot**:
   After setting up the environment and the dependencies, you can start the bot with the following command:
   ```bash
   python bot.py
   ```

2. **Bot Workflow**:
   - The bot opens Telegram Web and waits for the login screen.
   - It enters the provided password and waits for the user to appear in the chat list.
   - Once the user is available, the bot starts monitoring messages.
   - When a new message from the specified user is detected, it sends the message text to the generative AI model.
   - The AI model generates a response, which the bot sends back as a message.

## Files

- `bot.py`: The main script that runs the Telegram chatbot with AI integration.
- `.env`: A file to store sensitive information like API keys and passwords.
- `requirements.txt`: A list of dependencies required for the project.
- `chromedriver.exe`: The Selenium WebDriver for Chrome (ensure compatibility with your Chrome version).

## Dependencies

The project requires the following Python libraries:

- `selenium`: For automating browser interactions.
- `google-generativeai`: For accessing Google's Gemini AI model to generate responses.
- `python-dotenv`: For managing environment variables.

Install these dependencies using:
```bash
pip install selenium google-generativeai python-dotenv
```

## Configuration

Ensure that the following environment variables are configured correctly:

- **GEMINI_API_KEY**: Your Gemini API key (from Google Cloud).
- **TELEGRAM_PASSWORD**: The password for your Telegram Web account.
- **USER_ID**: The unique user ID of the individual whose messages the bot will respond to.

You can retrieve your user ID from the Telegram web interface or by using the Telegram API.

## Notes

- The script uses **Selenium WebDriver** to automate the browser actions, so ensure you have the correct version of **chromedriver** installed.
- The bot will continue running until manually stopped (e.g., by pressing `Ctrl+C`).
- Ensure that you handle the `.env` file securely and never share your credentials or API keys publicly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- Thanks to the [Selenium](https://www.selenium.dev/) project for providing browser automation.
- Thanks to [Google Cloud](https://cloud.google.com/) for their generative AI services.
- Thanks to the [Telegram Web](https://web.telegram.org/) platform for making chat automation possible.
