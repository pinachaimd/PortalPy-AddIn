import arcpy, pythonaddins, sys

#sys.path.append(".\Tools\Tools")
#2/15 Ash: Above searches for Tools\Tools in C:\Windows\System32 on Win8.

#Used to get SignOn working on Ash's machine:
tbxpath = r"C:\Users\Ashley\Documents\GitHub\PortalPy-AddIn\1021version\TestFailure\Install\Tools"
sys.path.append(tbxpath + "\\Tools")

import portalpy

global portalLogin

class SignIn(object):
    """Implementation for TestFailure_addin.button (Button)"""
    def __init__(self):
        
        self.enabled = True
        self.checked = False

    def onClick(self):

        #2/15 Ash: Reverted back to script tool Alex created in Install\Tools\Toolbox.
        #          Added pythonaddins to GPToolDialog and changed input parameter.
        
        portalLogin = pythonaddins.GPToolDialog(tbxpath + "\\Toolbox.tbx", "SignOn")
        
        #This is used to select datasets which is a possibility
        #value = pythonaddins.OpenDialog('Credentials', True, r'C:\'', 'Add')
        #I am thinking of just creating tools to do all of this then prompting
        #the button with: pythonaddins.GPToolDialog(toolbox, tool_name)
        
        if portalLogin == "True":
            #ButtonClass2.enabled = True
            print "True"
        else:
            print "False"

