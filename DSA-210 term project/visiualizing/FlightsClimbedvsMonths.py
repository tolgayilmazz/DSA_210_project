import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Load XML data
tree = ET.parse('aggregated_health_data321.xml')  # Replace with your file path
root = tree.getroot()

# Extract data into a DataFrame
data = []
for day in root.findall("Day"):
    date = day.get("date")
    flights_climbed = float(day.find("FlightsClimbed").text)
    data.append({"Date": date, "FlightsClimbed": flights_climbed})

df = pd.DataFrame(data)

# Convert Date to datetime for proper grouping
df["Date"] = pd.to_datetime(df["Date"])

# Extract month-year for grouping
df["Month"] = df["Date"].dt.to_period("M")

# Calculate the average flights climbed per month
monthly_flights_avg = (
    df.groupby("Month", as_index=False)["FlightsClimbed"].mean()
)

# Convert the "Month" column back to datetime for plotting
monthly_flights_avg["Month"] = monthly_flights_avg["Month"].dt.to_timestamp()

# Create the line graph
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_flights_avg["Month"],
    monthly_flights_avg["FlightsClimbed"],
    marker="o",
    linestyle="-",
    color="blue",
)
plt.title("Average Flights Climbed per Month")
plt.xlabel("Month")
plt.ylabel("Average Flights Climbed (count)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
