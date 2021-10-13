# SPIM3

Inverted lighsheet microscope built ontop of a confocal microscope base. Converting the confocal illumination into a lightsheet configuration, taking advantage of exisitng laser lines and scanning systems. System was designed to slide into an IX71 microscope base.


![System Schematic](/images/schematic.png)


Excitation from the confocal microscope is redirected to a 45 degree angle towards the excitation objective. During acqusition, the confocal draws a continuous line to generate a digital scanning light sheet. The fluoresence image is then acquired by a second objective orthagonal to the scanned light sheet and the image is projected onto the camera. 

## Components

### Microscope
IX71 Microscope Base  
FV300

### Optics
TL | Achromatic Doublet f = 150 mm ([AC254-150-A-ML](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-150-A-ML))

### Objectives
Obj1 | Olympus UMPLFLN10XW  
Obj2 | Olympus UMPLFLN20XW

### Camera
Cam | Photometrics Prime sCMOS

## TODO
- Filters
- Folder for CAD
- FOlder for software
