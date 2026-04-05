import pandas as pd
import mysql.connector

# 🔹 Step 1: Load CSV (comma separated)
df = pd.read_csv("data/campaign_data.csv")

# 🔹 Step 2: Clean column names (remove spaces)
df.columns = df.columns.str.strip()

# 🔹 Step 3: Handle missing values (optional but good)
df = df.fillna("")

# 🔹 Step 4: Check data
print("Preview Data:")
print(df.head())

# 🔹 Step 5: Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="dc_user",        # use this (recommended)
    password="1234",
    database="dcidb"
)

cursor = db.cursor()

# 🔹 Step 6: Insert data row by row
query = """
INSERT INTO campaigns (
    Campaign_ID, Campaign_Type, Target_Audience, Duration, Channel_Used,
    Impressions, Clicks, Leads, Conversions, Revenue,
    Acquisition_Cost, ROI, Language, Engagement_Score,
    Customer_Segment, Date
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    values = (
        str(row["Campaign_ID"]),
        str(row["Campaign_Type"]),
        str(row["Target_Audience"]),
        str(row["Duration"]),
        str(row["Channel_Used"]),
        str(row["Impressions"]),
        str(row["Clicks"]),
        str(row["Leads"]),
        str(row["Conversions"]),
        str(row["Revenue"]),
        str(row["Acquisition_Cost"]),
        str(row["ROI"]),
        str(row["Language"]),
        str(row["Engagement_Score"]),
        str(row["Customer_Segment"]),
        str(row["Date"])
    )

    cursor.execute(query, values)

# 🔹 Step 7: Commit changes
db.commit()

print("✅ Data Inserted Successfully!")

# 🔹 Step 8: Close connection
cursor.close()
db.close()