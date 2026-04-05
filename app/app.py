# app.py
from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="dc_user",
    password="1234",
    database="dcidb"
)
cursor = conn.cursor()

# Columns of campaigns table
FIELDS = ["Campaign_ID","Campaign_Type","Target_Audience","Duration","Channel_Used","Impressions",
          "Clicks","Leads","Conversions","Revenue","Acquisition_Cost","ROI","Language",
          "Engagement_Score","Customer_Segment","Date"]

@app.route('/')
def index():
    # Fetch latest 10 campaigns
    cursor.execute(f"SELECT * FROM campaigns ORDER BY Date DESC LIMIT 10")
    campaigns = [dict(zip(FIELDS, row)) for row in cursor.fetchall()]
    return render_template('index.html', campaigns=campaigns, fields=FIELDS)

@app.route('/add', methods=['POST'])
def add_data():
    # Get form data
    data = tuple(request.form[f] for f in FIELDS)
    # Insert into campaigns table
    sql = f"INSERT INTO campaigns ({', '.join(FIELDS)}) VALUES ({', '.join(['%s']*len(FIELDS))})"
    cursor.execute(sql, data)
    conn.commit()
    flash("Campaign added successfully!", "success")
    return redirect('/')

@app.route('/update/<campaign_id>', methods=['POST'])
def update_data(campaign_id):
    update_fields = [f for f in FIELDS if f != "Campaign_ID"]
    data = tuple(request.form[f] for f in update_fields)
    sql = f"UPDATE campaigns SET {', '.join([f'{f}=%s' for f in update_fields])} WHERE Campaign_ID=%s"
    cursor.execute(sql, data + (campaign_id,))
    conn.commit()
    flash("Campaign updated successfully!", "success")
    return redirect('/')

@app.route('/delete/<campaign_id>')
def delete_data(campaign_id):
    cursor.execute("DELETE FROM campaigns WHERE Campaign_ID=%s", (campaign_id,))
    conn.commit()
    flash("Campaign deleted successfully!", "success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)