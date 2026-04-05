README for Digital Campaign Dashboard
Project Name

Digital Campaign Dashboard – A Flask-based web application to manage and analyze digital marketing campaigns with a MySQL backend.

Project Overview

This project allows users to:

Add new campaigns via a web form
View campaigns in a clean dashboard
Perform basic CRUD operations (Create, Read, Update, Delete)
Clean and analyze campaign data using Python Pandas
Store cleaned data in a MySQL database

It simulates a real-world data pipeline:

CSV → MySQL → Pandas Cleaning → Clean Table → Flask Dashboard → GitHub Deployment

Features
Add new campaigns through a form
Display latest 10 campaigns in a table
Update or delete existing campaigns
Flash messages for success or error notifications
Data cleaning handled in Python before saving to SQL
Bootstrap 5 for responsive UI
Tech Stack
Backend: Python, Flask
Database: MySQL
Data Cleaning: Pandas
Frontend: HTML, Bootstrap 5
Version Control: Git, GitHub
Folder Structure
digital_campaign_dashboard/
│── app.py
│── analysisfold/
│   └── sql_cleaning.ipynb
│── templates/
│   └── index.html
│── static/         # optional: CSS, JS
│── requirements.txt
│── .gitignore
Setup & Installation
Clone the repo:
git clone https://github.com/prathmesh1001/digital_campaign_dashboard.git
cd digital_campaign_dashboard
Install dependencies:
pip install -r requirements.txt
Configure MySQL database:
Update app.py with your MySQL credentials:
conn = mysql.connector.connect(
    host="localhost",
    user="dc_user",
    password="1234",
    database="dcidb"
)
Run the Flask app:
python app.py
Open browser at http://127.0.0.1:5000/
Data Cleaning Steps (Pandas)
Load CSV or MySQL table into Pandas.
Remove duplicates.
Fill missing numeric values with mean or 0.
Fill missing text values with "Unknown".
Strip extra spaces from column names and values.
Convert numeric columns to proper types.
Save cleaned data back to SQL table (cleaned_campaigns) or CSV.
CRUD Operations in Flask
Create: Add new campaigns via form.
Read: Show latest 10 campaigns in the table.
Update: Edit existing campaigns (added later).
Delete: Remove campaigns (added later).
GitHub Version Control
Project was pushed to GitHub using:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/prathmesh1001/digital_campaign_dashboard.git
git push -u origin main
Future Improvements
Implement full update/delete functionality in UI.
Add charts & analytics for ROI, engagement, revenue.
Add user authentication for security.
Deploy app on Heroku / Render for public access.
Author

Prathmesh Mane

GitHub: prathmesh1001# digital_campaign_dashboard
