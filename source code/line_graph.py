import matplotlib.pyplot as plt

# Data for 2021-2023
years = [2021, 2022, 2023]

# 1. Oil Prices vs Inflation
oil_prices = [64.21, 70.68, 97.92]
inflation = [5.3, 6.7, 7.2]

plt.figure(figsize=(10, 5))
plt.plot(years, oil_prices, label='Oil Prices (USD)', color='blue', marker='o')
plt.plot(years, inflation, label='Inflation Rate (%)', color='red', marker='o')
plt.title('Oil Prices vs Inflation Rate (2021-2023)')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# 2. Fertilizer Prices vs Agricultural Inflation
fertilizer_prices = [315, 350, 420]
ag_inflation = [6.0, 7.3, 7.8]

plt.figure(figsize=(10, 5))
plt.plot(years, fertilizer_prices, label='Fertilizer Prices (Index)', color='green', marker='o')
plt.plot(years, ag_inflation, label='Agricultural Inflation (%)', color='orange', marker='o')
plt.title('Fertilizer Prices vs Agricultural Inflation (2021-2023)')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# 3. Trade Volume Between India and Russia
trade_volume = [10.2, 8.7, 6.5]

plt.figure(figsize=(10, 5))
plt.plot(years, trade_volume, label='Trade Volume (Billion USD)', color='purple', marker='o')
plt.title('India-Russia Trade Volume (2021-2023)')
plt.xlabel('Year')
plt.ylabel('Trade Volume (Billion USD)')
plt.legend()
plt.grid(True)
plt.show()

# 4. INR/USD Exchange Rate vs Import Prices
exchange_rate = [74.50, 77.25, 81.10]
import_prices = [103.5, 118.0, 135.2]

plt.figure(figsize=(10, 5))
plt.plot(years, exchange_rate, label='Exchange Rate (INR/USD)', color='blue', marker='o')
plt.plot(years, import_prices, label='Import Prices (Index)', color='red', marker='o')
plt.title('INR/USD Exchange Rate vs Import Prices (2021-2023)')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# 5. Commodity Prices vs Inflation
commodity_prices = [210, 275, 330]
inflation_rate = [5.3, 6.7, 7.2]

plt.figure(figsize=(10, 5))
plt.plot(years, commodity_prices, label='Commodity Prices (Index)', color='green', marker='o')
plt.plot(years, inflation_rate, label='Inflation Rate (%)', color='red', marker='o')
plt.title('Commodity Prices vs Inflation Rate (2021-2023)')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
