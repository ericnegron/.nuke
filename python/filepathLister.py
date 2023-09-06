# -----------------------------------------------------------------
#   filepathLister.py
#   Version: 1.0.0
#   Author: Eric Negrón 
#
#   Last Modified By: Eric Negrón 
#   Last Updated: September 5, 2023
# -----------------------------------------------------------------

# -----------------------------------------------------------------
#   USAGE:
#
#   - List all files being read into a nuke script.
# -----------------------------------------------------------------

import nuke
import os

def list_files():

    print("\n\nNuke Script: " + os.path.basename(nuke.root()['name'].value()))
    print("\nFILE & VERSION LIST: ")

    node_classes = ['Read', 'ReadGeo', 'Camera']
    node_list = []

    for node in nuke.allNodes():
        for nodeClass in node_classes:
            if node.knob('file') and node.Class() == nodeClass:
                node_list.append(node)

    for node in node_list:
        filepath = node['file'].value()
        filename = os.path.basename(filepath)

        filename_no_version = filename[0:filename.find('_v')]
        version_number = filename[filename.find('_v')+1 : filename.find('_v')+6]

        print("You are using " + version_number + " of " + filename_no_version)


