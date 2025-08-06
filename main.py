import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset into a DataFrame
df = pd.read_csv("data.csv")

# Quick preview of the data
print(df.head())

# Display dataset structure and data types
print("\n--- Dataset Info ---\n")
print(df.info())

# Check for missing values across all columns
print("\n--- Missing Values ---\n")
print(df.isnull().sum())

# Drop rows missing essential location info
df.dropna(subset=['source_center', 'destination_name', 'source_name'], inplace=True)

# Convert string time columns into datetime format for accurate time calculations
time_columns = ['trip_creation_time', 'od_start_time', 'od_end_time', 'cutoff_timestamp']
for col in time_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Confirm the datetime conversion
print("\n--- Data Types After Conversion ---\n")
print(df[time_columns].dtypes)

# ----------------------------------------
# Question 1: Delivery Duration Analysis
# ----------------------------------------

# Calculate delivery duration in minutes
df['delivery_duration_min'] = (df['od_end_time'] - df['od_start_time']).dt.total_seconds() / 60

# Show distribution stats for delivery duration
print("\n--- Delivery Duration (in minutes) ---\n")
print(df['delivery_duration_min'].describe())

# Average delivery time by route type (e.g., FTL vs Carting)
route_avg_duration = df.groupby("route_type")["delivery_duration_min"].mean().sort_values(ascending=False)
print(route_avg_duration)

# Bar chart for average delivery duration by route type
plt.figure(figsize=(6, 4))
route_avg_duration.plot(kind='bar', color='skyblue')
plt.title('Average Delivery Duration by Route Type')
plt.xlabel('Route Type')
plt.ylabel('Duration (minutes)')
plt.tight_layout()
plt.show()


# ----------------------------------------------------------
# Question 2: Count number of deliveries per source center
# ----------------------------------------------------------

source_counts = df['source_center'].value_counts()

# Top 5 most active source centers
print("\n--- Top 5 Source Centers ---")
print(source_counts.head())

# Bottom 5 least active source centers
print("\n--- Bottom 5 Source Centers ---")
print(source_counts.tail())

# Bar chart for top 5 most active source centers
plt.figure(figsize=(8, 4))
source_counts.head(5).plot(kind='bar', color='green')
plt.title('Top 5 Source Centers by Delivery Count')
plt.xlabel('Source Center')
plt.ylabel('Number of Deliveries')
plt.tight_layout()
plt.show()


# ----------------------------------------------
# Question 3: Compare OSRM Time vs Actual Time
# ----------------------------------------------

# Display summary stats for expected and actual delivery times
print("\n--- OSRM Time (Expected) ---\n")
print(df['osrm_time'].describe())

print("\n--- Actual Time (Real) ---\n")
print(df['actual_time'].describe())

# Calculate delay in minutes by subtracting expected from actual
df['delay_minutes'] = df['actual_time'] - df['osrm_time']

# Analyze delays across all trips
print("\n--- Delay in Minutes (Actual - OSRM) ---\n")
print(df['delay_minutes'].describe())

# Bar chart comparing average OSRM time and Actual delivery time
plt.figure(figsize=(6, 4))
time_comparison = {
    'OSRM Time (Expected)': df['osrm_time'].mean(),
    'Actual Time (Real)': df['actual_time'].mean()
}

plt.bar(time_comparison.keys(), time_comparison.values(), color=['blue', 'orange'])
plt.title('Expected vs Actual Delivery Time')
plt.ylabel('Time (minutes)')
plt.tight_layout()
plt.show()


# ----------------------------------------
# Question 4: Cutoff Compliance Ratio
# ----------------------------------------

# Count trips that met or missed cutoff deadlines
cutoff_counts = df['is_cutoff'].value_counts()
print("\n--- Cutoff Status Counts ---")
print(cutoff_counts)

# Calculate percentage of cutoff compliance
cutoff_percent = df['is_cutoff'].value_counts(normalize=True) * 100
print("\n--- Cutoff Status Percentage ---")
print(cutoff_percent)

# Pie chart for cutoff status
plt.figure(figsize=(5, 5))
cutoff_percent.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral'])
plt.title('Cutoff Compliance Ratio')
plt.ylabel('')
plt.tight_layout()
plt.show()

