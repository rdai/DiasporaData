import json
import pandas as pd
import os

# Load the CSV file
fileName = 'Nepalese'  #change this file name
base_path = r'D:\www\DiasporaData\data'
csv_file = os.path.join(base_path, f'{fileName}.csv')
csv_data = pd.read_csv(csv_file, dtype={'GEO_ID': str})
geojson_input = 'merged2021.geojson'
geojson_output = os.path.join(base_path, f'{fileName}.geojson')

# Load the CSV file
csv_data = pd.read_csv(csv_file, dtype={'GEO_ID': str})

# Load the GeoJSON file
with open(geojson_input, 'r') as f:
    geojson_data = json.load(f)

# Create a dictionary of GeoJSON features keyed by GEOID for quick lookup
geojson_dict = {feature['properties']['GEOID']: feature for feature in geojson_data['features']}

# Filter features and add population
filtered_features = []
unmatched_codes = []

for _, row in csv_data.iterrows():
    geo_id = row['GEO_ID']
    if geo_id in geojson_dict:
        feature = geojson_dict[geo_id]
        feature['properties']['population'] = int(row['B05006_001E'])
        feature['properties']['colorscale'] = int(row['COLORSCALE'])
        filtered_features.append(feature)
        print(f'Matched: {geo_id}')
    else:
        unmatched_codes.append(geo_id)
        print(f'Unmatched: {geo_id}')

# Create new GeoJSON with filtered features
filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

# Save the filtered and updated GeoJSON
with open(geojson_output, 'w') as f:
    json.dump(filtered_geojson, f)

print(f"GeoJSON file updated with {len(filtered_features)} features containing population data.")
print(f"Number of unmatched codes: {len(unmatched_codes)}")
print("Unmatched codes:", unmatched_codes)

# Optionally, save unmatched codes to a file
with open(os.path.join(base_path, f'{fileName}_unmatched_codes.txt'), 'w') as f:
    for code in unmatched_codes:
        f.write(f"{code}\n")