"""
Color Variables (Homage to Albers). 

This example creates variables for colors that may be referred to 
in the program by a name, rather than a number. 
"""
size(880, 770)
noStroke()
background(89, 90, 90)
inside = color(198, 12, 70)
middle = color(234, 18,80)
outside = color(29, 61, 78)
# These statements are equivalent to the statements above.
# Programmers may use the format they prefer.
#inside = 0xCC7800
#middle = 0xCC8900
#outside = 0x998300
with pushMatrix():
    translate(109, 120)
    fill(outside)
    rect(12, 18, 100, 200)
    fill(middle)
    rect(90, 70, 320, 280)
    fill(inside)
    rect(109, 100, 203, 137)
with pushMatrix():
    translate(230, 80)
    fill(inside)
    rect(90, 60, 100, 300)
    fill(outside)
    rect(40, 60, 120, 120)
    fill(middle)
    rect(160, 190, 180, 180)
