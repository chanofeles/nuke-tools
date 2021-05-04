## Standard Nuke tools I used on daily basis.
###Last updated v1 May 3 2021

##W_hotbox
import W_hotbox, W_hotboxManager

##KnobScripter
import KnobScripter

##ChannelHotbox
import channel_hotbox
nuke.menu("Nuke").findItem("Edit").addCommand("HotBox", 'channel_hotbox.start()', "alt+q")

##W_scaleTree
import W_scaleTree
nuke.menu('Nuke').addCommand('Edit/Node/W_scaleTree', 'W_scaleTree.scaleTreeFloatingPanel()', 'alt+`')


##JFX_nodeScaler
import JFX_nodeScaler
mNuke = nuke.menu("Nuke")
mMenu = mNuke.addMenu("MyMenu")
mMenu.addCommand('JFX_nodeScaler', JFX_nodeScaler.ScaleNodes)





#toolbar= nuke.toolbar("Nodes")
#toolbar.addCommand("Fer/MyGizmo","nuke.createNode('LightRebuild_audit')")

# V_EdgeMatte definitions
#toolbar = nuke.menu('Nodes')
#VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
#VMenu.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte")', icon='V_EdgeMatte.png')

##MirrorNodes
import mirrorNodes


###MergeTransforms
#import merge_transforms_v2
nuke.menu("Nuke").findItem("Edit").addCommand("merge_transforms", 'merge_transforms_v2.start()', 'alt+t')

###Stamps
import stamps


##ShuffleFromViewer
import shuffleFromViewer
