import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data for Monthly Temperature Line Plot
data_temp = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [30, 32, 45, 55, 65, 75, 80, 78, 70, 60, 50, 35]
}
df_temp = pd.DataFrame(data_temp)

# Data for Sales Bar Plot
data_sales = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [200, 300, 150, 400, 250]
}
df_sales = pd.DataFrame(data_sales)

# Data for Histogram
data_hist = np.random.randn(1000)

# Data for Scatter Plot with Regression Line
np.random.seed(0)
x = np.random.rand(100) * 100
y = 2.5 * x + np.random.normal(0, 10, size=x.shape)
df_scatter = pd.DataFrame({'X': x, 'Y': y})

# Plotting
plt.figure(figsize=(14, 10))

# Line Plot for Monthly Temperature
plt.subplot(2, 2, 1)
plt.plot(df_temp['Month'], df_temp['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)

# Bar Plot for Sales Data
plt.subplot(2, 2, 2)
sns.barplot(x='Product', y='Sales', data=df_sales, palette='viridis')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')

# Histogram of Random Data
plt.subplot(2, 2, 3)
plt.hist(data_hist, bins=30, edgecolor='black', alpha=0.7)
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Scatter Plot with Regression Line
plt.subplot(2, 2, 4)
sns.regplot(x='X', y='Y', data=df_scatter, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Scatter Plot with Regression Line')
plt.xlabel('X')
plt.ylabel('Y')

# Adjust layout and show plots
plt.tight_layout()
plt.show()
