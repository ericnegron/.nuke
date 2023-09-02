# -----------------------------------------------------------------
#   shuffleShortcuts.py
#   Version: 0.2.2
#
#   Last Modified By: Eric Negrón 
#   Last Updated: September 2, 2023
# -----------------------------------------------------------------

# -----------------------------------------------------------------
#   USAGE:
#
#   Creates a shuffle node that shuffles RGBA channels into the green channel.
# -----------------------------------------------------------------

import nuke

def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):
        
        # Create a new shuffle node
        shuffleNode = nuke.createNode('Shuffle')

        # Change input & output channels
        shuffleNode['in'].setValue(in_channel)
        shuffleNode['out'].setValue(out_channel)
        
        # Change knobs to green channel
        shuffleNode['red'].setValue(set_channel)
        shuffleNode['green'].setValue(set_channel)
        shuffleNode['blue'].setValue(set_channel)
        shuffleNode['alpha'].setValue(set_channel)
        
        # Change node color to match RGBA channels
        shuffleNode['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255, gColor*255, bColor*255, 1), 16))
        
        # Add node label
        shuffleNode['label'].setValue("[value red] > [value out]")
        
 
def shuffleRGBchannels():

        # Create Selected Node
        selectedNode = nuke.selectedNode()

        # Get X- & Y-Positions
        selectedNode_xPos = selectedNode['xpos'].value()
        selectedNode_yPos = selectedNode['ypos'].value()

        # Create RGB shuffles
        createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
        shuffleRed = nuke.selectedNode() 
        createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
        shuffleGreen = nuke.selectedNode()
        createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
        shuffleBlue = nuke.selectedNode()

        # Set R shuffle input and position
        shuffleRed.setInput(0, selectedNode)
        shuffleRed['xpos'].setValue(selectedNode_xPos - 150)
        shuffleRed['ypos'].setValue(selectedNode_yPos + 150)

        # Set G shuffle input and position
        shuffleGreen.setInput(0, selectedNode)
        shuffleGreen['xpos'].setValue(selectedNode_xPos)
        shuffleGreen['ypos'].setValue(selectedNode_yPos + 150)

        # Set B shuffle input and position
        shuffleBlue.setInput(0, selectedNode)
        shuffleBlue['xpos'].setValue(selectedNode_xPos + 150)
        shuffleBlue['ypos'].setValue(selectedNode_yPos + 150)


        # Merge shuffles 
        mergeNode = nuke.createNode('Merge2')
        mergeNode['operation'].setValue('max')
        mergeNode.setInput(1, shuffleRed)
        mergeNode.setInput(0, shuffleGreen)
        mergeNode.setInput(3, shuffleBlue)
        mergeNode['xpos'].setValue(selectedNode_xPos)
        mergeNode['ypos'].setValue(selectedNode_yPos + 300)



# Add to menu
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 1, 1, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "shuffleShortcuts.createCustomShuffle('alpha', 'rgba', 'alpha', 0, 1, 0)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB Channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)

 