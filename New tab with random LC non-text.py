#MenuTitle: New tab with random LC non-text
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Opens a new tab and outputs random lowercase non-text.
"""

import GlyphsApp
import time
import random
Glyphs.clearLog()
print "New tab with random LC non-text @ " + time.strftime("%H:%M:%S")

abecedary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
divisors = [3, 5, 7]
words = ""

for i in range(700):
    words = words + random.choice(abecedary)
    if i % random.choice(divisors) == 0:
        words = words + " "
Font.newTab(words)

print "Tab with random LC non-text opened."
