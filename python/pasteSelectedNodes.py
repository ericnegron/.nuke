# -----------------------------------------------------------------
#   pasteSelectedNodes.py
#   Version: 1.0.0
#   Author: Eric Negrón 
#
#   Last Modified By: Eric Negrón 
#   Last Updated: September 5, 2023
# -----------------------------------------------------------------

# -----------------------------------------------------------------
#   USAGE:
#
#   - Pastes previously copied node to all currently selected nodes.
# -----------------------------------------------------------------


import nuke

def paste_selected():

    for node in nuke.selectedNodes():
        node.setSelected(True)
        nuke.nodePaste("%clipboard%")
