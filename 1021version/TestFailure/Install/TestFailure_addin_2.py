import arcpy
import pythonaddins
import sys
#sys.path.append(".\Tools\Tools")

#To get it working on Ash's home machine.
tbxpath = r".\TestFailure\Install\Tools\Tools"
sys.path.append(tbxpath)

import portalpy

global portalLogin

class ButtonClass1(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        portalLogin = GPToolDialog(tbxpath + "\\Toolbox.tbx", "SignOn")
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
        if portalLogin == "True":
            #ButtonClass2.enabled = True
            print "True"
        else:
            print "False"

"""
"""
