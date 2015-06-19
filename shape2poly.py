######################################################################3
#
#  This script opens a shapefile and saves all objects within as 
#  APM MissionPlanner polygon-files. This enables the user to
#  use a set of polygons to generate survey plans. 
#
#
#  Read more about this script and other at:
#
#      http://www.mindland.com/wp/shapefiles-polyfiles
#

# Import standard libraries
import os,sys

# pyshp is the library used in by this script. It is available for
# download here:
#    https://code.google.com/p/pyshp/
#
# pyshp is licensed under the MIT-license:
#    http://opensource.org/licenses/mit-license.php
import shapefile


# V A R I A B L E S
#
# Check for command line variables
#
#if len(sys.argv) >0:
#    file_input   =   sys.argv[0]
#else:

# Name of the shapefile containing polygons.
# The file should be in the input-folder
file_input   = "grid_mindland"


# Set stem filename for output file
file_output = "grid_mindland_"


# Get current working directory
curr_wd     = os.getcwd()


# Set input and output directories
curr_input  = "%s/input/"  % (curr_wd)
curr_output = "%s/output/" % (curr_wd)

name_shapefile = ("%s%s") % (curr_input,file_input)


# Asssign shapefile to object 
sf = shapefile.Reader(name_shapefile)
shapes  = sf.shapes()

# Also get the records from the shapefile
records = sf.records()

counter = 0


# Work on shapefile objects
#
for shapeobject in shapes:
    
    # Filename code is here picked from two fields in the shapefile. 
    fileref = "%s-%s" % (records[counter][1], records[counter][0])
    
    # Activate this code to have a fileref which is just a number
    #fileref = str(counter)
    
    fname_subst = "%s.poly" % (fileref)
        
    # name file with name and number
    filename = "%s%s%s" % (curr_output, file_output, fname_subst)
    
    # ...and open the file for writing
    target = open (filename, 'w')
    
    # Write comment text in exported file with reference to this project and its author 
    target.write("#Saved from shapefile to poly script by Ragnvald Larsen \n")
    target.write("#(www.mindland.com) \n") 
    target.write("#\n")    
    
    # For each coordinate in the shapefile object...
    for coordinate in shapeobject.points: 
        
        # get coordinate string for current node in the polygon
        outstr = "%s %s" % (str(coordinate[1]), str(coordinate[0]))
        
        # Depending on settings on your computer you might end up using periods
        # instead of commas. This one makes sure the right stuff is used.
        outstr = str.replace(outstr, ".", ",")
        
        # Write coordinates to the file
        target.write(outstr)
        
        # add newline
        target.write("\n")
        
    # Close the file
    target.close()
    
    # Next record
    counter = counter+1    
    
    

        