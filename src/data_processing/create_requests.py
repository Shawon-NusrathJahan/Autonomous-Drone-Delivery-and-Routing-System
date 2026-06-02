import numpy as np       # numpy handles numerical operations and random numbers
import pandas as pd      # pandas creates and manages the DataFrame table
import os               # os helps us create folders and build file paths

def create_delivery_requests(
    num_requests=50,        # How many delivery orders to generate
    city_center=(22.3569, 91.7832),  # Chittagong city center (lat, lon)
    spread_km=5.0,          # How far from center deliveries can be, in km
    num_depots=3,           # How many drone launch bases (warehouses)
    seed=42                 # Seed makes random results reproducible — same seed = same data every time
):
    """
    Generates a synthetic drone delivery request dataset.
    
    Real drone delivery datasets have these features:
    - A depot (warehouse) where drones start
    - Customer locations that need deliveries
    - Package weights (affects drone battery usage)
    - Time windows (when the customer needs delivery)
    
    We simulate all of these so we can test routing algorithms
    even before the real datasets are available.
    """
    
    # Setting a seed means: if you run this with seed=42 tomorrow,
    # you get the exact same random numbers as today.
    # This is critical for reproducibility in research.
    np.random.seed(seed)
    
    # --- Convert spread from km to degrees ---
    # 1 degree of latitude ≈ 111 km anywhere on Earth
    # 1 degree of longitude ≈ 111 km × cos(latitude) — slightly less near the equator
    # For Chittagong (lat ≈ 22°), cos(22°) ≈ 0.927
    lat_spread = spread_km / 111.0
    lon_spread = spread_km / (111.0 * np.cos(np.radians(city_center[0])))
    
    # --- Generate customer delivery locations ---
    # np.random.uniform generates random numbers evenly spread between two values
    customer_lats = np.random.uniform(
        city_center[0] - lat_spread,   # southern boundary
        city_center[0] + lat_spread,   # northern boundary
        num_requests                    # how many points
    )
    customer_lons = np.random.uniform(
        city_center[1] - lon_spread,
        city_center[1] + lon_spread,
        num_requests
    )
    
    # --- Generate package weights (0.1 kg to 5.0 kg) ---
    # Most drone delivery packages are light — groceries, medicine, small electronics
    package_weights = np.random.uniform(0.1, 5.0, num_requests).round(2)
    
    # --- Generate time windows ---
    # Each customer has a preferred delivery window (e.g. between 9am and 12pm)
    # We represent time as minutes from midnight (0 = midnight, 540 = 9am)
    time_window_opens  = np.random.randint(480, 720, num_requests)  # 8am–12pm
    time_window_closes = time_window_opens + np.random.randint(60, 180, num_requests)  # 1–3 hour window
    
    # --- Generate priority levels ---
    # Priority 1 = urgent (medicine), Priority 3 = standard
    priorities = np.random.choice([1, 2, 3], num_requests, p=[0.1, 0.3, 0.6])
    
    # --- Generate depot (warehouse) locations ---
    # Depots are fixed bases — we place them near the city center with less spread
    depot_lats = np.random.uniform(
        city_center[0] - lat_spread * 0.3,
        city_center[0] + lat_spread * 0.3,
        num_depots
    )
    depot_lons = np.random.uniform(
        city_center[1] - lon_spread * 0.3,
        city_center[1] + lon_spread * 0.3,
        num_depots
    )
    
    # --- Build the customer DataFrame ---
    # pd.DataFrame creates a table from a dictionary.
    # Each key becomes a column name, each list becomes a column of values.
    customers_df = pd.DataFrame({
        'request_id':         range(1, num_requests + 1),
        'latitude':           customer_lats.round(6),
        'longitude':          customer_lons.round(6),
        'package_weight_kg':  package_weights,
        'time_window_open':   time_window_opens,
        'time_window_close':  time_window_closes,
        'priority':           priorities
    })
    
    # --- Build the depot DataFrame ---
    depots_df = pd.DataFrame({
        'depot_id':   range(1, num_depots + 1),
        'latitude':   depot_lats.round(6),
        'longitude':  depot_lons.round(6),
        'capacity':   [10, 8, 6][:num_depots]  # max drones per depot
    })
    
    return customers_df, depots_df


def save_synthetic_data(customers_df, depots_df, output_folder='../data/synthetic/'):
    """
    Saves the generated DataFrames as CSV files.
    Creates the folder if it does not already exist.
    """
    # os.makedirs creates the folder — exist_ok=True means no error if it already exists
    os.makedirs(output_folder, exist_ok=True)
    
    customers_path = os.path.join(output_folder, 'delivery_requests.csv')
    depots_path    = os.path.join(output_folder, 'depots.csv')
    
    # index=False means pandas does NOT write the row numbers as an extra column
    customers_df.to_csv(customers_path, index=False)
    depots_df.to_csv(depots_path,    index=False)
    
    print(f"Saved {len(customers_df)} delivery requests to: {customers_path}")
    print(f"Saved {len(depots_df)} depot locations to:    {depots_path}")