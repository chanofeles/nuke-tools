## Standard Nuke tools I used on daily basis.
###Last updated v4 Oct 17 2022

##W_hotbox
#import W_hotbox, W_hotboxManager

##KnobScripter
import KnobScripter

##ChannelHotbox
#import channel_hotbox
#nuke.menu("Nuke").findItem("Edit").addCommand("HotBox", 'channel_hotbox.start()', "alt+q")

##JFX_nodeScaler
# import JFX_nodeScaler
# mNuke = nuke.menu("Nuke")
# mMenu = mNuke.addMenu("Fernando")
# mMenu.addCommand('JFX_nodeScaler', JFX_nodeScaler.ScaleNodes)

##MirrorNodes
# import mirrorNodes

##ShuffleFromViewer
import shuffleFromViewer

##Stamps
import stamps

#Paste for all
import paste_for_all
FerMenu = nuke.menu('Nuke').addMenu('Fernando')
FerMenu.addCommand('Paste for all', 'paste_for_all.paste_for_all()', 'Shift+Ctrl+V')

#V_align nodes
import valign_nodes
FerMenu.addCommand('VerAlign Nodes', 'valign_nodes.valign_nodes()', 'Alt+Ctrl+Y')

#import distortion
import distortionImport
FerMenu.addCommand('Import lensDistortion', 'distortionImport.distortionImport()')

#import comp renders
import importCompVersions
FerMenu.addCommand('Import comp versions','importCompVersions.importCompVersions()')

#update to latest comp
import updateCompVersion
FerMenu.addCommand('Update to latest comp','updateCompVersion.updateCompVersion()')

#import shot  camera
import importCamera
FerMenu.addCommand('Import shot camera','importCamera.importCamera()')
