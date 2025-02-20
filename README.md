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


## Database Integration

This application is designed to track gold prices in real-time and send Telegram notifications when the price drops by a specified percentage. Currently, the functionality stores data temporarily in a list and does not use any persistent database. However, in a more advanced version of the application, the following features could be added:

### Database Usage

- **Persistent Data Storage**: Price data can be stored in a database (e.g., SQLite, PostgreSQL, MySQL). This allows access to historical data and enables advanced operations such as trend analysis.
- **Data Analysis**: Perform analyses on the data stored in the database (e.g., calculating average prices, identifying highest/lowest prices).
- **Scalability**: Using a database allows the application to scale for larger use cases, such as tracking prices for multiple users or different assets.

### Why Is It Not Necessary Now?

- **Simplicity**: The current application is designed to meet basic needs such as real-time price tracking and notifications. Database integration could complicate the functionality and unnecessarily consume resources.
- **Temporary Data Storage**: The application stores price data temporarily in a list, which provides a simple and fast solution.
- **Rapid Prototyping**: This project was developed to quickly prototype and test core functionality. Database integration can be considered as a step for future enhancements.

### Future Enhancements

If the application is to be developed into a more professional version, the following steps can be taken:

1. **Database Selection**: Choose a database such as SQLite, PostgreSQL, or MongoDB.
2. **Data Modeling**: Create a suitable data model for price data (e.g., fields such as date, price, asset type).
3. **API Integration**: Develop a REST API or GraphQL API for accessing the database.
4. **Dashboard Creation**: Add a dashboard for users to visualize historical data.
5. **JASP or SPSS**: Can visualize or make predictions about price based on the data
