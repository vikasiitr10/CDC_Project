
import requests
import os
import pandas as pd
from tqdm import tqdm

def download_images(excel_path, output_folder, mapbox_token):
    # Load Data
    if not os.path.exists(excel_path):
        print(f"Error: File not found at {excel_path}")
        return

    df = pd.read_excel(excel_path)
    os.makedirs(output_folder, exist_ok=True)

    print(f"Starting download for {len(df)} properties...")

    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        house_id = row['id']
        lat = row['lat']
        lon = row['long']
        
        filename = f"{output_folder}/{house_id}.jpg"
        
        # Skip if exists
        if os.path.exists(filename):
            continue

        url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},17,0/500x500?access_token={mapbox_token}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            print(f"Error downloading {house_id}: {e}")

    print("Download process completed.")

# Note: To run this script, a user would import this function or add a main block.
