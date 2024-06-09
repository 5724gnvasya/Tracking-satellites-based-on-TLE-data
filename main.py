import sys
# from src import api_shp, make_png
import api_shp, make_png
from datetime import date

if __name__ == '__main__':
    if len(sys.argv)!= 6:
        print("Usage: python main.py <id> <year> <month> <day> <step>")
        sys.exit(1)

    sat_id = int(sys.argv[1])
    year = int(sys.argv[2])
    month = int(sys.argv[3])
    day = int(sys.argv[4])
    step = int(sys.argv[5])

    date_obj = date(year, month, day)

    api_shp.create_orbital_track_shapefile_for_day(sat_id, date_obj, step)
    make_png.make_png(sat_id)

# api_shp.create_orbital_track_shapefile_for_day(sat_id, date(year, mounth, day), step_minutes)
# make_png.make_png(sat_id)