## Standard Nuke tools I used on daily basis.
###Last updated v4 Oct 17 2022

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

##ShuffleFromViewer
import shuffleFromViewer
