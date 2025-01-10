import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Load the monthly averages XML data
tree = ET.parse('monthly_averages.xml')  # Replace with your file path
root = tree.getroot()

# Extract data into a DataFrame
data = []
for month in root.findall("Month"):
    name = month.get("name")
    active_energy = float(month.find("AverageActiveEnergyBurned").text)
    flights_climbed = float(month.find("AverageFlightsClimbed").text)
    data.append({"Month": name, "AverageActiveEnergyBurned": active_energy, "AverageFlightsClimbed": flights_climbed})

df = pd.DataFrame(data)

# Convert Month to datetime for proper plotting
df["Month"] = pd.to_datetime(df["Month"])

# Create scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(df["AverageActiveEnergyBurned"], df["AverageFlightsClimbed"], alpha=0.7, color="blue", s=100)

# Add month names to each data point
for i, row in df.iterrows():
    plt.text(
        row["AverageActiveEnergyBurned"], 
        row["AverageFlightsClimbed"], 
        row["Month"].strftime('%b %Y'),  # Format as 'MMM YYYY'
        fontsize=10, ha="right"
    )

# Add titles and labels
plt.title("Scatter Plot of Monthly Averages: Active Energy Burned vs Flights Climbed")
plt.xlabel("Average Active Energy Burned (kcal)")
plt.ylabel("Average Flights Climbed (count)")
plt.grid(True)
plt.show()
