import xml.etree.ElementTree as ET
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Parse the XML file
file_path = 'aggregated_health_data321.xml'  # Update the path if necessary
tree = ET.parse(file_path)
root = tree.getroot()

# Extract data from XML
data = []
for day in root.findall('Day'):
    date = day.get('date')
    active_energy = float(day.find('ActiveEnergyBurned').text)
    flights_climbed = float(day.find('FlightsClimbed').text)
    data.append({'Date': date, 'ActiveEnergyBurned': active_energy, 'FlightsClimbed': flights_climbed})

# Create a DataFrame
df = pd.DataFrame(data)

# Remove rows with zero ActiveEnergyBurned as they may not contribute meaningfully
df = df[df['ActiveEnergyBurned'] > 0]

# Separate features and target
X = df[['FlightsClimbed']]
y = df['ActiveEnergyBurned']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color="blue", label="Actual Values")
plt.scatter(X_test, y_pred, color="red", label="Predicted Values")
plt.title("Actual vs Predicted Active Energy Burned")
plt.xlabel("Flights Climbed")
plt.ylabel("Active Energy Burned")
plt.legend()
plt.grid()
plt.show()

# Plot regression line on the full dataset
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.title("Regression Line for Active Energy Burned Prediction")
plt.xlabel("Flights Climbed")
plt.ylabel("Active Energy Burned")
plt.legend()
plt.grid()
plt.show()
