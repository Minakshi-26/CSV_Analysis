# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ CSV file read karna
df = pd.read_csv('sales_data.csv')  # Apni CSV ka naam yaha change kar sakti ho
print("Data Loaded:\n", df.head(), "\n")

# 2️⃣ Total Sales per Product
total_sales = df.groupby('Product')['Sales'].sum()
print("Total Sales per Product:\n", total_sales, "\n")

# 3️⃣ Highest & Lowest Selling Product
highest_product = total_sales.idxmax()
lowest_product = total_sales.idxmin()
print(f"Highest Selling Product: {highest_product} - {total_sales[highest_product]}")
print(f"Lowest Selling Product: {lowest_product} - {total_sales[lowest_product]}\n")

# 4️⃣ Total Sales per Region
region_sales = df.groupby('Region')['Sales'].sum()
print("Total Sales per Region:\n", region_sales, "\n")

# 5️⃣ Save Summary CSV
summary = total_sales.reset_index()
summary.to_csv('sales_summary.csv', index=False)
print("Summary saved to sales_summary.csv\n")

# 6️⃣ Visualization

# a) Product-wise Bar Chart
total_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# b) Region-wise Pie Chart
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Region')
plt.show()
