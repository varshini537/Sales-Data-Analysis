import pandas as pd

# Load dataset
data = pd.read_csv('sales_data.csv')

# Total sales
total_sales = data['Sales'].sum()

# Average sales
avg_sales = data['Sales'].mean()

# Highest sale
max_sales = data['Sales'].max()

print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Highest Sale:", max_sales)