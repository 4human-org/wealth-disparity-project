import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the provided CSV data
file_path = '/data/dfa-networth-levels.csv'
wealth_data = pd.read_csv(file_path)

# Data preprocessing
# Splitting the 'Date' column into year and quarter
wealth_data[['Year', 'Quarter']] = wealth_data['Date'].str.split(':Q', expand=True)

# Converting 'Year' and 'Quarter' to integers
wealth_data['Year'] = wealth_data['Year'].astype(int)
wealth_data['Quarter'] = wealth_data['Quarter'].astype(int)

# Creating a datetime column by combining 'Year' and 'Quarter'
wealth_data['Datetime'] = pd.to_datetime(wealth_data['Year'].astype(str) + 'Q' + wealth_data['Quarter'].astype(str))

# Sorting data by 'Datetime'
wealth_data.sort_values(by='Datetime', inplace=True)

# Pivot the table for easier plotting
pivot_data = wealth_data.pivot(index='Datetime', columns='Category', values='Net worth')

# Plotting the data
plt.figure(figsize=(15, 8))
sns.lineplot(data=pivot_data)
plt.title('US Wealth Distribution Over Time by Population Segment')
plt.xlabel('Year')
plt.ylabel('Net Worth (in Billion $)')
plt.legend(title='Population Segment')
plt.grid(True)
plt.show()
