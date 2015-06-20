# -*- coding: utf-8 -*-
""" Split a shapefile to several .poly files :
http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format
"""
import os,sys
import shapefile

def shp2polys(shp_file, dest_dir):
    sf = shapefile.Reader(shp_file)
    shapes  = sf.shapes()

    records = sf.records()
    counter = 0
    for shapeobject in shapes:
        dept_code = records[counter][0]
        output_name = "departement-{}.poly".format(dept_code)
        with open (os.path.join(dest_dir, output_name), 'w') as target:
            target.write("Departement {}\n".format(dept_code))		
            target.write("1\n".format(dept_code))		
            for coords in shapeobject.points:
                coords_str = "{} {}".format(coords[1], coords[0]).replace(".", ",")
                target.write("{}\n".format(coords_str))		
            target.write("END\nEND\n".format(coords_str))		
        counter = counter + 1

