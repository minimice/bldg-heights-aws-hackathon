import geopandas as gpd
import os

df_fp = gpd.read_file('DC_Buildings_Footprint_4326_test.geojson')
fp_test = df_fp[0:100]

fp_test.to_csv('DC_Buildings_Footprint_4326_small_test.csv')