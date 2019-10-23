import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point

#Read LAS file
inFile = File("C:/Users/anarayanan/Downloads/1714.las", mode = "r")

#Import LAS into numpy array (X=raw integer value x=scaled float value)
#Note that the column
lidar_points = np.array((inFile.X,inFile.Y,inFile.Z,inFile.intensity,
                          inFile.classification, inFile.gps_time, 
                          inFile.overlap, inFile.scan_angle )).transpose()

#Transform to pandas DataFrame
lidar_df=DataFrame(lidar_points, columns = ["X","Y","Z","intensity",
                "classification","gps_time","overlap","scan_angle"])

#Transform to geopandas GeoDataFrame
crs = None
geometry = [Point(xyz) for xyz in zip(inFile.X,inFile.Y,inFile.Z)]
lidar_geodf = GeoDataFrame(lidar_df, crs=crs, geometry=geometry)

# set correct coordinate reference system
lidar_geodf.crs = {'init': 'epsg:6487'}
