# -*- coding: utf-8 -*-
# Inspired from 
import os,sys

# pyshp is the library used in by this script. It is available for
# download here:
#    https://code.google.com/p/pyshp/
#
# pyshp is licensed under the MIT-license:
#    http://opensource.org/licenses/mit-license.php
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
            for coords in shapeobject.points:
                coords_str = "{} {}".format(coords[1], coords[0]).replace(".", ",")
                target.write("{}\n".format(coords_str))		
        counter = counter + 1

