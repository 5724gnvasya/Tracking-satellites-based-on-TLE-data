import requests
import matplotlib.colors as mcolors
import pandas as pd
from pyorbital.orbital import Orbital
import datetime
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from flask import flash, redirect # was needed for showing error messages

def add_id(new_id):
    df = pd.read_csv('curr.csv')
    df = df._append({'Satellite': new_id, 'colour': ''}, ignore_index=True)
    df.to_csv('curr.csv', index=False)

def remove_id(id_to_remove):
    df = pd.read_csv('curr.csv')
    df = df[df['Satellite'] != id_to_remove]
    df.to_csv('curr.csv', index=False)
def remove_all_ids():
    df = pd.DataFrame(columns=['Satellite', 'colour'])
    df.to_csv('curr.csv', index=False)
def fetch_tle_data():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    response = requests.get(url)
    response.raise_for_status()
    tle_lines = response.text.splitlines()
    satellites = []
    for i in range(0, len(tle_lines), 3):
        if i + 2 < len(tle_lines):
            sat_name = tle_lines[i].strip()
            tle_line1 = tle_lines[i + 1].strip()
            tle_line2 = tle_lines[i + 2].strip()
            satellites.append({
                "Satellite": sat_name,
                "TLE Line 1": tle_line1,
                "TLE Line 2": tle_line2
            })
    tle_df = pd.DataFrame(satellites)
    tle_df.to_csv('test_tle.csv', index=False)

def make_other():
    print("Entering make_other() function")
    # global error_message
    # error_message = None
    orbital = None
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    start_time = datetime.datetime.now(datetime.timezone.utc)
    times = [start_time + datetime.timedelta(seconds=60 * i) for i in range(90)]
    df = pd.read_csv('curr.csv')
    df1 = pd.read_csv('test_tle.csv')
    for _, row in df.iterrows():
        sat_id = row['Satellite']
        color = row['colour']
        curr = df1[df1['Satellite'] == sat_id]
        tle1 = curr['TLE Line 1'].values[0]
        tle2 = curr['TLE Line 2'].values[0]
        try:
            orbital = Orbital(sat_id, line1=tle1, line2=tle2)
            lons = []
            lats = []
            for time in times:
                lon, lat, _ = orbital.get_lonlatalt(time)
                lons.append(lon)
                lats.append(lat)
            ax.plot(lons, lats, markersize=5, color=color, linestyle='-', transform=ccrs.Geodetic())
            ax.plot(lons[0], lats[0], marker='o', markersize=5, color=color, transform=ccrs.Geodetic())
            

        except:
            df = pd.read_csv('curr.csv')
            df = df[df['Satellite'] != sat_id]
            df.to_csv('curr.csv', index=False)
            # error_message = f"Error processing satellite {sat_id}: {str(Exception)}"
            print("Error processing satellite", sat_id)
            # return error_message
            
            # flash(f"Error processing satellite {sat_id}", "danger")

   
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    fig.tight_layout()
    plt.savefig('satellites.png', bbox_inches='tight')


def assign_colours():
    df = pd.read_csv('curr.csv')
    num_ids = len(df)
    if num_ids > 0:
        colormap = plt.get_cmap('inferno', num_ids)
        df['colour'] = [mcolors.rgb2hex(colormap(i / num_ids)[:3]) for i in range(num_ids)]
    df.to_csv('curr.csv', index=False)


def initialize_csv():
    df = pd.DataFrame(columns=['Satellite', 'colour'])
    df.to_csv('curr.csv', index=False)