import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load XML data
tree = ET.parse('aggregated_health_data321.xml')  # Replace with your file path
root = tree.getroot()

# Extract data into a DataFrame
data = []
for day in root.findall("Day"):
    date = day.get("date")
    active_energy = float(day.find("ActiveEnergyBurned").text)
    flights_climbed = float(day.find("FlightsClimbed").text)
    data.append({"Date": date, "ActiveEnergyBurned": active_energy, "FlightsClimbed": flights_climbed})

df = pd.DataFrame(data)

# Extract x (Active Energy Burned) and y (Flights Climbed)
x = df["ActiveEnergyBurned"]
y = df["FlightsClimbed"]

# Fit a polynomial of degree 2
poly_func = np.polyfit(x=x, y=y, deg=2)

# Generate x values for the fitted curve
xp = np.linspace(start=x.min(), stop=x.max(), num=50)

# Evaluate the polynomial
yp = np.polyval(p=poly_func, x=xp)

# Calculate the standard deviation
sigma = np.std(y - np.polyval(p=poly_func, x=x))

# Plot the polynomial fit curve
plt.plot(xp, yp, color="#111111", alpha=0.8, linewidth=1, label="Polynomial Fit (Degree 2)")

# Add the shaded area for ±1 standard deviation
plt.fill_between(x=xp, y1=yp - sigma, y2=yp + sigma, color="#222222", alpha=0.2, label="±1 Std. Dev.")

# Scatter plot of original data
plt.scatter(x, y, s=10, color="#AD2D56", label="Original Data")

# Add labels and legend
plt.title("Scatter Plot with Polynomial Fit and Std. Deviation")
plt.xlabel("Active Energy Burned (kcal)")
plt.ylabel("Flights Climbed (count)")
plt.legend()
plt.grid(True)
plt.show()
