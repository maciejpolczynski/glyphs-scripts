#MenuTitle: Display previous layer
# -*- coding: utf-8 -*-
# slightly adapted by Pedro Arilla from a @mekkablue's (Rainer Erich Scheichelbauer) snippet
# source: https://forum.glyphsapp.com/t/keyboard-shortcuts-for-the-layers-palette/6578/2
__doc__="""
Switches to the previous layer of the current glyph.

Recommended keyboard shortcut: Ctrl+UPArrow
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Display previous layer @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
currentTab = thisFont.currentTab
if thisFont and currentTab:
	currentLayer = currentTab.activeLayer()
	if currentLayer:
		currentGlyph = currentLayer.parent
		availableLayers = currentGlyph.layers
		currentIndex = availableLayers.index(currentLayer)
		previousIndex = (currentIndex-1)%len(availableLayers)
		previousLayer = availableLayers[previousIndex]
		offset = currentTab.layersCursor
		newLayers = currentTab.layers[:]
		newLayers.insert(offset,previousLayer)
		newLayers.pop(offset+1)
		currentTab.layers = newLayers

print "Previous layer active."
