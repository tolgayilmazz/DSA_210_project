import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Data from XML
data = {
    "Month": [
        "2023-10", "2023-11", "2023-12", "2024-01", "2024-02",
        "2024-03", "2024-04", "2024-05", "2024-06"
    ],
    "AverageActiveEnergyBurned": [
        683.25, 604.99, 694.28, 666.72, 556.00,
        635.68, 602.28, 705.69, 341.50
    ],
    "AverageFlightsClimbed": [
        22.17, 30.14, 28.00, 25.38, 18.05,
        12.79, 13.64, 15.50, 1.20
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Perform Pearson correlation test
correlation, p_value = stats.pearsonr(
    df["AverageActiveEnergyBurned"],
    df["AverageFlightsClimbed"]
)

# Calculate t-value
n = len(df)  # Sample size
t_value = correlation * np.sqrt((n - 2) / (1 - correlation ** 2))

# Display results
print(f"Pearson correlation coefficient: {correlation:.3f}")
print(f"T-value: {t_value:.3f}")
print(f"P-value: {p_value:.3f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(
    df["AverageActiveEnergyBurned"],
    df["AverageFlightsClimbed"],
    color="blue", label="Data points"
)

# Add regression line
slope, intercept, _, _, _ = stats.linregress(
    df["AverageActiveEnergyBurned"],
    df["AverageFlightsClimbed"]
)
x_vals = df["AverageActiveEnergyBurned"]
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color="red", label="Regression line")

# Label the plot
plt.title("Correlation between Active Energy Burned and Flights Climbed")
plt.xlabel("Average Active Energy Burned")
plt.ylabel("Average Flights Climbed")
plt.legend()
plt.grid()

# Show the plot
plt.show()
