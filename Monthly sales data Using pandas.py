import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your actual file path)
df = pd.read_csv('C:\\Users\\ADMIN\\Videos\\Captures\\New folder\\New folder\\New folder\\New folder\\sales_data.csv')


# Display first 5 rows and check for missing values
print(df.head())
print(df.isnull().sum())

# Handle missing values (drop or fill)
df = df.dropna()

# Add Total Sales column
df['Total Sales'] = df['Quantity'] * df['Price']

# Extract month from Date
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# Aggregate monthly sales
monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()

# Find best and worst months
best_month = monthly_sales.loc[monthly_sales['Total Sales'].idxmax()]
worst_month = monthly_sales.loc[monthly_sales['Total Sales'].idxmin()]

print(f"Best Month: {best_month}")
print(f"Worst Month: {worst_month}")

# Analyze sales by region
sales_by_region = df.groupby('Region')['Total Sales'].sum().reset_index()

# Visualizations
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['Month'], monthly_sales['Total Sales'], color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales')
plt.xticks(monthly_sales['Month'])
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(sales_by_region['Total Sales'], labels=sales_by_region['Region'], autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Region')
plt.show()

# Save the results to a CSV file
monthly_sales.to_csv('monthly_sales_summary.csv', index=False)
