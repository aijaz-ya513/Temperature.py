import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Sample time series data
data = {
    'Date': ['2025-07-25', '2025-07-26', '2025-07-27', '2025-07-28', '2025-07-29','2025-07-30',],
    'Temperature': [35, 37, 39, 40, 39,37]
}
df = pd.DataFrame(data)
# Step 2: Convert to datetime and set index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# Step 3: Plot
df.plot()
plt.title("📈 Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()