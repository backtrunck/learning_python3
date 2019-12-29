# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:32:45 2018

@author: luiscar
"""
import os
from osgeo import ogr

caminho = "..//datasets_geospatial//thematic_mapping.org//TM_WORLD_BORDERS-0.3.shp"
if not os.path.exists(caminho):
    exit(1)

shapefile = ogr.Open(caminho)
layer = shapefile.GetLayer(0)

countries = [] #List of code, name, min/max Lat/Long tuples

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    
    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")
    
    geometry = feature.GetGeometryRef()
    
    minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
    
    countries.append((countryName, countryCode, minLat, maxLat,\
                      minLong, maxLong))
countries.sort()

for name, code, minLat, maxLat, minLong, maxLong in countries:
    print("{} ({}) lat = {:0.4f},{:0.4f} lon = {:0.4f},{:0.4f}".format(name,\
          code, minLat, maxLat, minLong, maxLong))
    