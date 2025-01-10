import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Load and parse the XML file
tree = ET.parse('aggregated_health_data321.xml') 
root = tree.getroot()

# Extract data and exclude outliers
data = []
for day in root.findall("Day"):
    date = day.get("date")
    active_energy = float(day.find("ActiveEnergyBurned").text)

    if active_energy == 0:  # Ignore zero values
        continue

    data.append({"Date": date, "ActiveEnergyBurned": active_energy})

# Create a DataFrame
df = pd.DataFrame(data)

# Convert dates to datetime and extract months
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

# Calculate average active energy burned per month
monthly_active_energy_avg = df.groupby("Month", as_index=False)["ActiveEnergyBurned"].mean()

# Convert Month to datetime for plotting
monthly_active_energy_avg["Month"] = monthly_active_energy_avg["Month"].dt.to_timestamp()

# Create the line graph
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_active_energy_avg["Month"],
    monthly_active_energy_avg["ActiveEnergyBurned"],
    marker="o",
    linestyle="-",
    color="orange",
)
plt.title("Average Active Energy Burned per Month (Excluding Outliers)")
plt.xlabel("Month")
plt.ylabel("Average Active Energy Burned (kcal)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
