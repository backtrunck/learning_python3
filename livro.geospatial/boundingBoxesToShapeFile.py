# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:32:45 2018

@author: luiscar
"""
import os, shutil

from osgeo import ogr
from osgeo import osr


pasta = "..//datasets_geospatial//thematic_mapping.org//"

scrNmArquivo = os.path.join(pasta,"TM_WORLD_BORDERS-0.3.shp")
dstNmPasta = os.path.join(pasta,"bounding.box")

if not os.path.exists(scrNmArquivo):
    exit(1)


#Open the source shapefile
scrFile = ogr.Open(scrNmArquivo)

scrLayer = scrFile.GetLayer(0)

#open the output shapefile

if os.path.exists(dstNmPasta):
    shutil.rmtree(dstNmPasta)

os.mkdir(dstNmPasta)

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

driver = ogr.GetDriverByName("ESRI Shapefile")
dstPath = os.path.join(dstNmPasta, "boundingBoxes.shp")
dstFile = driver.CreateDataSource(dstPath)
dstLayer = dstFile.CreateLayer("layer", spatialReference)

fieldDef = ogr.FieldDefn("COUNTRY", ogr.OFTString)
fieldDef.SetWidth(50)
dstLayer.CreateField(fieldDef)

fieldDef = ogr.FieldDefn("CODE", ogr.OFTString)
fieldDef.SetWidth(3)
dstLayer.CreateField(fieldDef)

countries = [] #List of code, name, min/max Lat/Long tuples

for i in range(scrLayer.GetFeatureCount()):
    
    feature = scrLayer.GetFeature(i)
    
    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")
    
    geometry = feature.GetGeometryRef()
    
    minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
    
    linearRing = ogr.Geometry(ogr.wkbLinearRing)
    linearRing.AddPoint(minLong, minLat)
    linearRing.AddPoint(maxLong, minLat)
    linearRing.AddPoint(maxLong, maxLat)
    linearRing.AddPoint(minLong, maxLat)
    linearRing.AddPoint(minLong, minLat)
    
    polygon = ogr.Geometry(ogr.wkbPolygon)
    polygon.AddGeometry(linearRing)
    
    feature = ogr.Feature(dstLayer.GetLayerDefn())
    feature.SetGeometry(polygon)
    feature.SetField("COUNTRY",countryName)
    feature.SetField("CODE",countryCode)
    dstLayer.CreateFeature(feature)
    feature.Destroy()
#all done

scrFile.Destroy()
dstFile.Destroy()
    