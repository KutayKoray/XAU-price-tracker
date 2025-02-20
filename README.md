#💰🔔 Gold Price Tracking and Telegram Notification System

This project tracks gold prices from [Investing.com](https://www.investing.com/) and sends Telegram notifications when the price drops by a specified percentage. The project is developed using Python and Selenium.

---

## 📌 Features

- **Gold Price Tracking**: Fetches real-time gold prices from Investing.com.
- **Telegram Notifications**: Sends notifications via Telegram when the price drops by a certain percentage.
- **Customizable Threshold**: The percentage drop can be adjusted by the user.
- **Headless Mode**: Can run the browser in headless (invisible) mode.

---

## 🛠 Installation

### Requirements

- Python 3.8 or higher
- Chrome or Chromium browser
- ChromeDriver (for Selenium)

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/gold-price-tracker.git
   cd gold-price-tracker

### Create a Virtual Environment and Install Dependencies:

```bash
  Copy
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  pip install -r requirements.txt
```

Create a Telegram Bot:

Create a new bot using @BotFather on Telegram.

Obtain the bot's API Token and your Chat ID.
