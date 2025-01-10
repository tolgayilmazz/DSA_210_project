import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd

# Load the XML file
input_file_path = 'aggregated_health_data321.xml'
tree = ET.parse(input_file_path)
root = tree.getroot()

# Parse the data and filter outliers
data = []
for day in root.findall("Day"):
    date = day.get("date")
    active_energy = float(day.find("ActiveEnergyBurned").text)
    flights_climbed = float(day.find("FlightsClimbed").text)

    if active_energy == 0:  # Ignore outliers with zero active energy
        continue

    data.append({
        "Date": datetime.strptime(date, "%Y-%m-%d"),
        "ActiveEnergyBurned": active_energy,
        "FlightsClimbed": flights_climbed
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Group by month and calculate averages
df["Month"] = df["Date"].dt.to_period("M")
monthly_avg = df.groupby("Month").mean()[["ActiveEnergyBurned", "FlightsClimbed"]].reset_index()

# Build the output XML structure
root = ET.Element("MonthlyAverages")
for _, row in monthly_avg.iterrows():
    month_element = ET.SubElement(root, "Month", name=str(row["Month"]))
    active_energy_element = ET.SubElement(month_element, "AverageActiveEnergyBurned")
    active_energy_element.text = f"{row['ActiveEnergyBurned']:.2f}"
    flights_climbed_element = ET.SubElement(month_element, "AverageFlightsClimbed")
    flights_climbed_element.text = f"{row['FlightsClimbed']:.2f}"

# Write the output XML file
output_path = "monthly_averages.xml"
tree = ET.ElementTree(root)
tree.write(output_path, encoding="utf-8", xml_declaration=True)
print(f"Monthly averages XML file saved to {output_path}")
