import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

# Data for 2021-2023 (converted for regression analysis)
years = [2021, 2022, 2023]

# Data for regression analysis
data = pd.DataFrame({
    'Year': years,
    'Oil_Price': [64.21, 70.68, 97.92],
    'Fertilizer_Price': [315, 350, 420],
    'Exchange_Rate': [74.50, 77.25, 81.10],
    'Inflation': [5.3, 6.7, 7.2],
    'Ag_Inflation': [6.0, 7.3, 7.8],
    'Import_Prices': [103.5, 118.0, 135.2]
})

# 1. Oil Prices vs Inflation (Regression)
X_oil = sm.add_constant(data['Oil_Price'])  # Independent variable (Oil Prices)
Y_inflation = data['Inflation']  # Dependent variable (Inflation)
model_oil_inflation = sm.OLS(Y_inflation, X_oil).fit()
print(model_oil_inflation.summary())

# Plotting Oil Prices vs Inflation
plt.figure(figsize=(10, 6))
plt.scatter(data['Oil_Price'], data['Inflation'], color='blue', label='Data Points')

# Polynomial regression for better fitting
poly_oil = np.polyfit(data['Oil_Price'], data['Inflation'], 2)
poly_oil_line = np.poly1d(poly_oil)
plt.plot(data['Oil_Price'], poly_oil_line(data['Oil_Price']), color='red', label='Polynomial Regression Line')

plt.title('Oil Prices vs Inflation (2021-2023)', fontsize=14)
plt.xlabel('Oil Prices (USD per Barrel)', fontsize=12)
plt.ylabel('Inflation Rate (%)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 2. Fertilizer Prices vs Agricultural Inflation (Regression)
X_fertilizer = sm.add_constant(data['Fertilizer_Price'])  # Independent variable (Fertilizer Prices)
Y_ag_inflation = data['Ag_Inflation']  # Dependent variable (Agricultural Inflation)
model_fertilizer_inflation = sm.OLS(Y_ag_inflation, X_fertilizer).fit()
print(model_fertilizer_inflation.summary())

# Plotting Fertilizer Prices vs Agricultural Inflation
plt.figure(figsize=(10, 6))
plt.scatter(data['Fertilizer_Price'], data['Ag_Inflation'], color='green', label='Data Points')

# Polynomial regression for better fitting
poly_fertilizer = np.polyfit(data['Fertilizer_Price'], data['Ag_Inflation'], 2)
poly_fertilizer_line = np.poly1d(poly_fertilizer)
plt.plot(data['Fertilizer_Price'], poly_fertilizer_line(data['Fertilizer_Price']), color='red', label='Polynomial Regression Line')

plt.title('Fertilizer Prices vs Agricultural Inflation (2021-2023)', fontsize=14)
plt.xlabel('Fertilizer Prices (Index)', fontsize=12)
plt.ylabel('Agricultural Inflation Rate (%)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 3. Exchange Rate vs Import Prices (Regression)
X_exchange = sm.add_constant(data['Exchange_Rate'])  # Independent variable (Exchange Rate)
Y_import = data['Import_Prices']  # Dependent variable (Import Prices)
model_exchange_import = sm.OLS(Y_import, X_exchange).fit()
print(model_exchange_import.summary())

# Plotting Exchange Rate vs Import Prices
plt.figure(figsize=(10, 6))
plt.scatter(data['Exchange_Rate'], data['Import_Prices'], color='orange', label='Data Points')

# Polynomial regression for better fitting
poly_exchange = np.polyfit(data['Exchange_Rate'], data['Import_Prices'], 2)
poly_exchange_line = np.poly1d(poly_exchange)
plt.plot(data['Exchange_Rate'], poly_exchange_line(data['Exchange_Rate']), color='red', label='Polynomial Regression Line')

plt.title('Exchange Rate vs Import Prices (2021-2023)', fontsize=14)
plt.xlabel('Exchange Rate (INR/USD)', fontsize=12)
plt.ylabel('Import Prices (Index)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()