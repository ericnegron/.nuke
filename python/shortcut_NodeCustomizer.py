# -----------------------------------------------------------------
#   shortcut_NodeCustomizer.py
#   Version: 1.0.0
#   Author: Eric Negrón 
#
#   Last Modified By: Eric Negrón 
#   Last Updated: March 21, 2024
# -----------------------------------------------------------------

# -----------------------------------------------------------------
#   USAGE:
#
#   - Adds shortcut to change a node's label, easily add
#     the value of a knoob to the label, and 
#     set teh color of the node.
# -----------------------------------------------------------------

import nuke

def customize_node():
    
    # Define variables 
    selectedNode = nuke.selectedNode()
    oldComment = selectedNode['label'].value()
    knoblist = []

    # Get all the knobs from the selected node
    for knob in selectedNode.knobs():
        knoblist.append(knob)

    knoblist.sort()
    knoblist.insert(0, 'None')

    knoblist_string = " ".join(knoblist)

    # Create a panel
    panel = nuke.Panel('Node Customizer')

    panel.addSingleLineInput('Comment:', oldComment)
    panel.addEnumerationPulldown('Knob', knoblist_string)
    panel.addBooleanCheckBox('Change Node Color?', False)

    # Do nothing if cancel button pressed 
    if not panel.show():
        return


    comment_input = panel.value('Comment')
    knob_choice = panel.value('Knob')
    node_label = comment_input + "\n" + knob_choice + ": [value " + knob_choice + "]"

    # Update the node label
    if comment_input == "" and panel.value("Knob") == "None":
        if panel.value("Change Node Color?") == False:
            nuke.message("Please enter a node label")        
    elif knob_choice == "None":
        selectedNode['label'].setValue(comment_input)
    elif comment_input == "":
        selectedNode['label'].setValue(knob_choice + ": [value " + knob_choice + "]")
    else:
        selectedNode['label'].setValue(node_label)

    # Handle node color checkbox
    if panel.value('Change Node Color?') == True:
        selectedNode['title_color'].setValue(nuke.getColor())
    else:
        return
    

nuke.menu('Nuke').addCommand('Utilities/Node Customizer', 'shortcut_NodeCustomizer.customize_node()', 'ctrl+alt+c')