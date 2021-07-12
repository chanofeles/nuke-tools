## Standard Nuke tools I used on daily basis.
###Last updated v2 Jun 22 2021

##W_hotbox
import W_hotbox, W_hotboxManager

##KnobScripter
import KnobScripter

##ChannelHotbox
import channel_hotbox
nuke.menu("Nuke").findItem("Edit").addCommand("HotBox", 'channel_hotbox.start()', "alt+q")

##JFX_nodeScaler
import JFX_nodeScaler
mNuke = nuke.menu("Nuke")
mMenu = mNuke.addMenu("Fernando")
mMenu.addCommand('JFX_nodeScaler', JFX_nodeScaler.ScaleNodes)

##MirrorNodes
import mirrorNodes

###MergeTransforms
import merge_transforms_v2
nuke.menu("Nuke").findItem("Edit").addCommand("merge_transforms", 'merge_transforms_v2.start()', 'alt+t')


##ShuffleFromViewer
import shuffleFromViewer



#toolbar= nuke.toolbar("Nodes")
#toolbar.addCommand("Fer/MyGizmo","nuke.createNode('LightRebuild_audit')")

# V_EdgeMatte definitions
#toolbar = nuke.menu('Nodes')
#VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
#VMenu.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte")', icon='V_EdgeMatte.png')
