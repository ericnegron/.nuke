# -----------------------------------------------------------------
#  menu.py
#  Version: 1.0.1
#  Last Updated: August 29, 2023
# -----------------------------------------------------------------


# -----------------------------------------------------------------
#  GLOBAL IMPORTS :::::::::::::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

import nuke
import platform
import nukescripts

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


nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass="FrameHold")

# -----------------------------------------------------------------
#  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

utlitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utlitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

customGizmosMenu = nuke.menu('Nodes').addMenu('CustomGizmos', icon="myGizmos_icon.png")
customGizmosMenu.addCommand('Breakdownerizationer', 'nuke.createNode("Breakdownerizationer")')


# -----------------------------------------------------------------
#  CUSTOM KEYBOARD SHORTCUTS ::::::::::::::::::::::::::::::::::::::
# -----------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)
