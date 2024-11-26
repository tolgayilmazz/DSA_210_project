# Correlation Between Flights Climbed and Active Energy Burned

## Project Description
This project explores the relationship between daily **Flights Climbed** and **Active Energy Burned** using personal health data from Apple Health. The data covers a period during my second year of university, where I lived on:
- 3rd floor during the first term.
- Entrance floor during the second term.

The primary goal is to assess whether the dormitory floor level influenced my active energy burned and to quantify the correlation between flights climbed and energy burned.


## Dataset
The dataset consists of two key metrics:
- Flights Climbed: Number of floors climbed daily.
- Active Energy Burned: Energy burned in calories.

The dataset spans:
- First Term: While living on the 3rd floor.
- Second Term: While living on the entrance floor.


## Objectives
1. Correlation Analysis:
   - Investigate the relationship between flights climbed and active energy burned.
2. Impact Assessment:
   - Compare the metrics between the two terms to evaluate how the dormitory floor level affected physical activity and energy expenditure.


## Plan

### Step 1: Data Parsing
- Extract the relevant metrics (FlightsClimbed and ActiveEnergyBurned) from the **Apple Health export.xml** file.
- Preprocess the data:
  - Convert timestamps to datetime.
  - Filter data for the relevant terms.

### Step 2: Data Analysis and Visualization
1. Descriptive Analysis:
   - Calculate daily averages for both metrics.
   - Compare statistics between the two terms.
2. Correlation Analysis:
   - Use statistical techniques (e.g., Pearson correlation) to measure the relationship between flights climbed and active energy burned.
   - Create scatterplots to visualize this correlation.
3. Term Comparison:
   - Divide the data into two subsets (first term and second term).
   - Use bar charts or box plots to compare the metrics across terms.

### Step 3: Interpretation and Conclusion
- Summarize findings about the correlation between flights climbed and active energy burned.
- Assess the impact of living on different floors on physical activity and energy expenditure.

