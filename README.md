# Streamlit NFL/CFB Score Management App

### Overview
- This Streamlit app allows users to manage NFL and College Football (CFB) game data, including inserting, updating, and deleting records. The app toggles between NFL and CFB data, providing an easy-to-use interface for managing game results.

### Features
- Toggle between NFL and CFB: Switch between managing NFL and CFB data.
- Insert Game Data: Add new games with teams, scores, and locations.
- Update Existing Data: Modify game scores and other details.
- Delete Records: Remove games from the database with confirmation.
- Concurrency Handling: Notifies users if a game has been updated by someone else.

### Requirements
- Python 3.8+
- Streamlit
- MySQL
MySQL Connector for Python

### Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Python Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up MySQL Database:

Ensure MySQL is installed and running.
Create the databases for NFL and CFB using the provided SQL scripts:
bash
Copy code
mysql -u your_username -p < Build_NFL_Tables.sql
mysql -u your_username -p < Build_CFB_Tables.sql

### Configure Database Connections:

Update the database connection details in the Streamlit app code.
python
Copy code
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="nfl_db"  # or "cfb_db" based on user selection
)

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

Open your web browser and go to http://localhost:8501.
### Usage
- Select League: Use the dropdown to choose between NFL and CFB data.
- Insert a New Game: Fill out the form with the game date, teams, scores, and location, then submit.
- Update a Game: Choose an existing game to modify its details.
- Delete a Game: Confirm the deletion of a game from the database.

### Contributing
If you would like to contribute, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the existing style guidelines.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
If you have any questions or suggestions, feel free to reach out via GitHub Issues.

Notes:
Replace "your-username" and "your-repo-name" with your actual GitHub username and repository name.
Ensure your requirements.txt file includes all necessary Python packages (streamlit, mysql-connector-python, etc.).
Customize any sections to better fit your project’s specifics.
