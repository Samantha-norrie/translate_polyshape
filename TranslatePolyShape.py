#Import
import maya.cmds as cmds
from functools import partial

#Function to translate polyshape
def translate(slider, *args, **kwargs):
    value = getSliderValue(slider)
    cmds.move(value, **kwargs)

#Function for slider value
def getSliderValue(ctrlName):
    value = cmds.floatSlider(ctrlName, q=True, value=True)
    return value
 
#Function to reset location and sliders to [0, 0, 0]    
def reset():
    cmds.move(0.00, 0.00, 0.00) 
    windowUI()  

#Window
def windowUI():
    #If window exists, delete it
    if(cmds.window('TranslatePolyShape', exists=True)):
        cmds.deleteUI('TranslatePolyShape')
    theWin = cmds.window('TranslatePolyShape')    
    cmds.columnLayout( adjustableColumn=True, w=500, columnAlign='center', rowSpacing=20)  
                                              
    #Create sliders and text
    cmds.text('\n', height=2)
    cmds.text('X Axis', font='boldLabelFont', height=10)
    xSlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.text('Y Axis', font='boldLabelFont')
    ySlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.text('Z Axis', font='boldLabelFont')
    zSlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.text('\n', height=2)
    cmds.floatSlider(xSlider, e=True, dc = partial(translate, xSlider, x=0.5))
    cmds.floatSlider(ySlider, e=True, dc = partial(translate, ySlider, y=0.5))
    cmds.floatSlider(zSlider, e=True, dc = partial(translate, zSlider, z=0.5))
    cmds.button(label='Reset', height=40, command='reset()')
    cmds.showWindow()  
windowUI()      