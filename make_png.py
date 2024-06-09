import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def make_png(sat_id):
    gdf = gpd.read_file(f'{sat_id}.shp')
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.plot(gdf.geometry.x, gdf.geometry.y, marker='o', markersize=5, color='blue', linestyle='-', transform=ccrs.Geodetic())
    for i, row in gdf.iterrows():
        ax.annotate(row['TIME'], xy=(row.geometry.x, row.geometry.y), ha='center', va='center', fontsize=8, transform=ccrs.Geodetic())
    ax.set_title('Satellite trajectory')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    # plt.savefig(f'{sat_id}.png')
    # plt.show()
    plt.savefig(f'{sat_id}.png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)  # Close the figure to free up memory
