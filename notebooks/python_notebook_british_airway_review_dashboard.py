# Python Notebook - British Airway Review Dashboard

"""
# New Notebook
"""

# Install dependencies
import matplotlib.pyplot as plt # Draw chart
import pandas as pd # Hold dataframe
import seaborn as sns # Draw hearmap

# Load data
df = pd.read_csv('data/review.csv')

# Drop Null values
df_cleaned = df.dropna()

# Process SEAT_TYPE
eco_df = df_cleaned[df_cleaned['SEAT_TYPE'] == 'Economy Class'] 
non_eco_df = df_cleaned[df_cleaned['SEAT_TYPE'] != 'Economy Class']

# Select relevant columns for correlation calculation
numeric_cols = ['AVERAGE_RATING', 'FOOD_AND_BEVERAGES', 'GROUND_SERVICE', 
                'SEAT_COMFORT', 'CABIN_STAFF_SERVICE', 'WIFI_AND_CONNECTIVITY',
                'VALUE_FOR_MONEY']
                
# Correlation matrix for Economy Class
eco_corr = eco_df[numeric_cols].corr()

# Correlation matrix for Non-Economy Class
non_eco_corr = non_eco_df[numeric_cols].corr()


# Create heatmap for Economy Class
plt.figure(figsize=(5, 5))
sns.heatmap(eco_corr, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title("Correlation Heatmap - Economy Class")
plt.show()


# Create heatmap for Economy Class
plt.figure(figsize=(5, 5))
sns.heatmap(non_eco_corr, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title("Correlation Heatmap - Non Economy Class")
plt.show()




