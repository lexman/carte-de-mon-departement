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
            start_idx = 0
            end_idxs = [p for p in shapeobject.parts][1:] + [len(shapeobject.points)]
            poly_num = 1
            for end_idx in end_idxs:
                target.write("{}\n".format(poly_num))
                for coords in shapeobject.points[start_idx:end_idx]:
                    coords_str = "    {}    {}".format(coords[0], coords[1]).replace(",", ".")
                    target.write("{}\n".format(coords_str))
                target.write("END\n")
                start_idx = end_idx    
            target.write("END\n")
        counter = counter + 1
