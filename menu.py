# -----------------------------------------------------------------
#  menu.py
#  Version: 1.0.7
#  Last Updated: September 6, 2023
# -----------------------------------------------------------------


# -----------------------------------------------------------------
#  GLOBAL IMPORTS :::::::::::::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

import nuke
import platform
import nukescripts
from NukeTools import NukeServerSocket

# Define .nuke directory path
MacOSX_Dir = '/Users/ericnegron/.nuke'
Linux_Dir = ''
Win_Dir = ''

# Set Global directory
if platform.system() == "Windows":
    dir = Win_Dir
elif platform.system() == "Darwin":
    dir = MacOSX_Dir
elif platform.system() == "Linux":
    dir = Linux_Dir
else:
    dir = None
    
         
# -----------------------------------------------------------------
#  KNOB DEFAULTS  :::::::::::::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

# MOTION BLUR SHUTTER - CENTERED
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")

# Tracker Defaults
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

# Frame Hold Default
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass="FrameHold")


# -----------------------------------------------------------------
#  CUSTOM KEYBOARD SHORTCUTS ::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

# Tracker Shortcut
nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)


# Merge Node Shortcuts
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")
mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Add.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="From.png", shortcutContext=2)

# Paste Selected Shortcut
nuke.menu('Nuke').addCommand('Edit/Paste to Selected', 'pasteSelectedNodes.paste_selected()', 'ctrl+shift+v')



# -----------------------------------------------------------------
#  CUSTOM PYTHON SCRIPTS     ::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------
import shuffleShortcuts
import filepathLister
import pasteSelectedNodes

# -----------------------------------------------------------------
#  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
utilitiesMenu.addCommand('List Files', 'filepathLister.list_files()')

customGizmosMenu = nuke.menu('Nodes').addMenu('CustomGizmos', icon="myGizmos_icon.png")
customGizmosMenu.addCommand('Breakdownerizationer', 'nuke.createNode("Breakdownerizationer")')

