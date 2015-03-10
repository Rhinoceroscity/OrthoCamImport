'''
Created on Jan 21, 2015

@author: cgi-28
'''
from pymel.core import windows, system, general
import os

class orthoCams():
    def __init__(self):
        print("Init Vars")
        self.initVars()
        print("Init GUI")
        self.initGUI()
        print("Load Values")
        self.loadValues()
    
    def initVars(self):
        #Initialize a bunch of variables that are going to come in handy later
        self.currentQualitySetting = "high"
        self.locked = True
        self.saveDir = os.path.join(os.path.expanduser("~"), "Documents/orthoCams/")
        #if not os.path.isdir(self.saveDir):
        #    os.makedirs(self.saveDir)
            
        self.infoNode = "CamerasInfoNode"
        
        self.cameraApertureSelections = [["Nikon D7100 (23.5x15.6mm)",0.9251969,0.6141732],
                                         ["Canon 5D Mark 3 (36x24mm)",1.41732,0.944882]]
        
        self.cameraGroups = ["front_Center_CamGrp",
                             "Front_3_4_CamGrp",
                             "Profile_CamGrp",
                             "Rear_3_4_CamGrp",
                             "Rear_Center_CamGrp",]
        
        self.cameras=["front_Center_CAM",
                      "Front_3_4_CAM",
                      "Profile_CAM",
                      "Rear_3_4_CAM",
                      "Rear_Center_CAM"]
        
        self.cameraShapes=["front_Center_CAMShape",
                      "Front_3_4_CAMShape",
                      "Profile_CAMShape",
                      "Rear_3_4_CAMShape",
                      "Rear_Center_CAMShape"]
        
        self.highQualityFilePathEntries = ["oc_frontHighQualityTextField",
                                     "oc_front34HighQualityTextField",
                                     "oc_sideHighQualityTextField",
                                     "oc_back34HighQualityTextField",
                                     "oc_backHighQualityTextField"]
        
        self.lowQualityFilePathEntries = ["oc_frontLowQualityTextField",
                                     "oc_front34LowQualityTextField",
                                     "oc_sideLowQualityTextField",
                                     "oc_back34LowQualityTextField",
                                     "oc_backLowQualityTextField"]
        
        self.imagePlanes = ["Front_Center_ImagePlane",
                            "Front_3_4_ImagePlane",
                            "Profile_imagePlane",
                            "Rear_3_4_ImagePlane",
                            "Rear_Center_ImagePlane"]
                
    def loadValues(self):
        if general.objExists(self.infoNode):
            windows.floatSliderGrp("oc_FocalLengthSliderGrp", e = True, v = general.getAttr(self.infoNode + ".cameraFocalLength"))
            
            windows.textFieldGrp("oc_frontHighQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".highQualityFrontCenterImage", ""))
            windows.textFieldGrp("oc_front34HighQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".highQualityFront34Image", ""))
            windows.textFieldGrp("oc_sideHighQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".highQualitySideImage", ""))
            windows.textFieldGrp("oc_back34HighQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".highQualityRear34Image", ""))
            windows.textFieldGrp("oc_backHighQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".highQualityRearCenterImage", ""))
        
            windows.textFieldGrp("oc_frontLowQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".lowQualityFrontCenterImage", ""))
            windows.textFieldGrp("oc_front34LowQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".lowQualityFront34Image", ""))
            windows.textFieldGrp("oc_sideLowQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".lowQualitySideImage", ""))
            windows.textFieldGrp("oc_back34LowQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".lowQualityRear34Image", ""))
            windows.textFieldGrp("oc_backLowQualityTextField", e = True, tx = general.getAttr(self.infoNode + ".lowQualityRearCenterImage", ""))
        
    def setImagePlaneTextures(self, _type = "high"):
        if _type == "high":
            for index, i in enumerate(self.imagePlanes):
                filePath = windows.textFieldGrp(self.highQualityFilePathEntries[index], q = True, tx = True)
                if os.path.isfile(filePath):
                    general.setAttr(i+".imageName", filePath)
                else:
                    print("Not valid path")
        else:
            for index, i in enumerate(self.imagePlanes):
                filePath = windows.textFieldGrp(self.lowQualityFilePathEntries[index], q = True, tx = True)
                if os.path.isfile(filePath):
                    general.setAttr(i+".imageName", filePath)
                else:
                    print("Not valid path")
    
    def toggleLockedValues(self):
        if "Cameras" in general.ls(tr = True):
            if self.locked == False:
                self.locked = True
            else:
                self.locked = False
            
            if self.locked == True:
                windows.button("oc_LockButton", e = True, l = "Unlock Cameras")
                for i in self.cameras:
                    general.setAttr(i + ".translateX", l = self.locked)
                    general.setAttr(i + ".translateY", l = self.locked)
                    general.setAttr(i + ".translateZ", l = self.locked)
                    general.lockNode(i, l = self.locked)
                
                for j in self.cameraGroups:
                    general.setAttr(j + ".translateX", l = self.locked)
                    general.setAttr(j + ".translateY", l = self.locked)
                    general.setAttr(j + ".translateZ", l = self.locked)
                    general.setAttr(j + ".rotateX", l = self.locked)
                    general.setAttr(j + ".rotateY", l = self.locked)
                    general.setAttr(j + ".rotateZ", l = self.locked)
                    general.setAttr(j + ".scaleX", l = self.locked)
                    general.setAttr(j + ".scaleY", l = self.locked)
                    general.setAttr(j + ".scaleZ", l = self.locked)
                    general.lockNode(j, l = self.locked)
    
            else:
                windows.button("oc_LockButton", e = True, l = "Lock Cameras")
                for j in self.cameraGroups:
                    general.lockNode(j, l = self.locked)
                    general.setAttr(j + ".translateX", l = self.locked)
                    general.setAttr(j + ".translateY", l = self.locked)
                    general.setAttr(j + ".translateZ", l = self.locked)
                    general.setAttr(j + ".rotateX", l = self.locked)
                    general.setAttr(j + ".rotateY", l = self.locked)
                    general.setAttr(j + ".rotateZ", l = self.locked)
                    general.setAttr(j + ".scaleX", l = self.locked)
                    general.setAttr(j + ".scaleY", l = self.locked)
                    general.setAttr(j + ".scaleZ", l = self.locked)
                    
                for i in self.cameras:
                    general.lockNode(i, l = self.locked)
                    general.setAttr(i + ".translateX", l = self.locked)
                    general.setAttr(i + ".translateY", l = self.locked)
                    general.setAttr(i + ".translateZ", l = self.locked)
    
    def updateImagePlanePaths(self):
        general.setAttr(self.infoNode + ".highQualityFrontCenterImage", windows.textFieldGrp("oc_frontHighQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".highQualityFront34Image", windows.textFieldGrp("oc_front34HighQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".highQualitySideImage", windows.textFieldGrp("oc_sideHighQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".highQualityRear34Image", windows.textFieldGrp("oc_back34HighQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".highQualityRearCenterImage", windows.textFieldGrp("oc_backHighQualityTextField", q = True, tx = True))
        
        general.setAttr(self.infoNode + ".lowQualityFrontCenterImage", windows.textFieldGrp("oc_frontLowQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".lowQualityFront34Image", windows.textFieldGrp("oc_front34LowQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".lowQualitySideImage", windows.textFieldGrp("oc_sideLowQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".lowQualityRear34Image", windows.textFieldGrp("oc_back34LowQualityTextField", q = True, tx = True))
        general.setAttr(self.infoNode + ".lowQualityRearCenterImage", windows.textFieldGrp("oc_backLowQualityTextField", q = True, tx = True))
        self.updateCurrentImagePlaneText()
        
    def updateCurrentImagePlaneText(self):
        if "Cameras" in general.ls(tr = True):
            general.setAttr(self.imagePlanes[0] + ".imageName", general.getAttr(self.infoNode + "." + self.currentQualitySetting + "QualityFrontCenterImage",""))
            general.setAttr(self.imagePlanes[1] + ".imageName", general.getAttr(self.infoNode + "." + self.currentQualitySetting + "QualityFront34Image",""))
            general.setAttr(self.imagePlanes[2] + ".imageName", general.getAttr(self.infoNode + "." + self.currentQualitySetting + "QualitySideImage",""))
            general.setAttr(self.imagePlanes[3] + ".imageName", general.getAttr(self.infoNode + "." + self.currentQualitySetting + "QualityRear34Image",""))
            general.setAttr(self.imagePlanes[4] + ".imageName", general.getAttr(self.infoNode + "." + self.currentQualitySetting + "QualityRearCenterImage",""))
    
    def toggleImageQuality(self):
        if "Cameras" in general.ls(tr = True):
            if self.currentQualitySetting == "high":
                self.currentQualitySetting = "low"
                
            else:
                self.currentQualitySetting = "high"
            
            self.updateCurrentImagePlaneText()
        #self.setImagePlaneTextures(self.currentQualitySetting)
        #windows.button("oc_toggleLowHighQualityButton", e = True, l = "Switch to %s Quality"%(self.currentQualitySetting))
                       
    def loadImage(self, slot):
        #The slot argument should contain the access name of the appropriate text field
        _filters = "All Files (*.*);;TIFF (*.tif *.tiff);;PNG (*.png);;JPEG (*.jpg *.jpeg);;EXR (*.exr)"
        _file = system.fileDialog2(fm = 1, ff = _filters)
        if _file!=None:
            windows.textFieldGrp(slot, e = True, tx = _file[0])
            self.updateImagePlanePaths()
            
    def setFocalLengthAll(self):
        #for i in self.cameraShapes:
        if "Cameras" in general.ls(tr = True):
            general.setAttr(self.infoNode+".cameraFocalLength", windows.floatSliderGrp("oc_FocalLengthSliderGrp", q = True, v = True))
    
    def setCameraAperture(self):
        #for i in self.cameraShapes:
        if "Cameras" in general.ls(tr = True):
            val = windows.optionMenu("oc_CameraApertureSelector", q = True, sl = True) - 1
            general.setAttr(self.infoNode+".cameraApertureHorizontal", self.cameraApertureSelections[val][1])
            general.setAttr(self.infoNode+".cameraApertureVertical", self.cameraApertureSelections[val][2])
        
    def importCameras(self):
        #camerasPath = "/Volumes/Creative/research-development/Resource/Utilities/scenes/orthoCameras.ma"
        camerasPath = "/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/orthoCameras.ma"
        if os.path.isfile(camerasPath) and not "Cameras" in general.ls(tr = True):
            self.locked=True
            print(general.ls(tr = True))
            system.importFile(camerasPath)
    
    def deleteCameras(self):
        if "Cameras" in general.ls(tr = True):
            if self.locked==True:
                self.toggleLockedValues()
                
            general.select("Cameras")
            general.select("Cameras", hi = True)
            general.delete()
            
            cleanupObjs = [
                           "orthoCameras_Driver_Profile_imagePlane",
                           "orthoCameras_Front_3_4_ImagePlane",
                           "orthoCameras_Front_Center_ImagePlane",
                           "orthoCameras_Profile_imagePlane",
                           "orthoCameras_Rear_3_4_ImagePlane",
                           "orthoCameras_Rear_Center_ImagePlane",
                           "orthoCameras_front_Center_imagePlane",
                           "orthoCameras_sceneConfigurationScriptNode",
                           "orthoCameras_uiConfigurationScriptNode",
                           "orthoCameras_wiper_Position",
                           "orthoCameras_Driver_Profile_imagePlane1",
                           "orthoCameras_Rear_3_4_imagePlane",
                           "orthoCameras_Rear_Center_imagePlane",
                           "Driver_Profile_imagePlane1",
                           "Front_3_4_ImagePlane",
                           "Front_Center_ImagePlane",
                           "Profile_imagePlane",
                           "Rear_3_4_ImagePlane",
                           "Rear_3_4_imagePlane",
                           "Rear_Center_imagePlane",
                           "front_Center_imagePlane",
                           "Rear_Center_ImagePlane"]
            
            for obj in cleanupObjs:
                if general.objExists(obj):
                    general.delete(obj)
    
    def initGUI(self):
        if windows.window("orthoCams", exists = True):
            windows.deleteUI("orthoCams")
        windows.window("orthoCams", t = "Ortho Cam Manager", sizeable = False)
        windows.columnLayout()
        ##-Body of UI
        
        windows.rowLayout(nc = 2)
        windows.button("oc_ImportCamerasFile", l = "Import Ortho Cameras", w = 250, h = 25, c = lambda x: self.importCameras())
        windows.button("oc_DeleteCamerasFile", l = "Delete Ortho Cameras", w = 250, h = 25, c = lambda x: self.deleteCameras())
        windows.setParent(u = True)
        
        windows.frameLayout("oc_TopFrameLayout", l = "Camera Settings",w = 500)
        
        windows.rowLayout(nc = 2)
        windows.button("oc_toggleLowHighQualityButton", l = "Toggle Quality", w = 250, h = 25, c = lambda x: self.toggleImageQuality())
        windows.button("oc_LockButton", l = "Unlock Cameras", w = 250, h = 25, c = lambda x: self.toggleLockedValues())
        windows.setParent(u = True)

        windows.rowLayout(nc = 2)
        windows.floatSliderGrp("oc_FocalLengthSliderGrp" , l = "Focal Length", field = True, min = 5, max = 300, v = 200, pre = 0, cw3 = [70,50,150], cc = lambda x: self.setFocalLengthAll())
        windows.optionMenu("oc_CameraApertureSelector", l = "Camera Aperture" , cc = lambda x: self.setCameraAperture())
        [windows.menuItem(l = name[0], p = "oc_CameraApertureSelector") for name in self.cameraApertureSelections]
        windows.setParent(u = True)
        windows.setParent(u = True)
        windows.separator(h=10, w = 500, st = "in")
        ##Bottom Frame
        windows.frameLayout("oc_BottomFrameLayout",l = "Image Settings", w = 500)
        windows.rowLayout(nc = 2)
        ####
        ####Left Frame
        ####
        windows.columnLayout()
        windows.text("High Quality Images")

        #Left
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_frontHighQualityTextField", l = "Front", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_frontHighQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_frontHighQualityTextField"))
        windows.setParent(u = True)
        #Left 3/4
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_front34HighQualityTextField", l = "Front 3/4", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_front34HighQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_front34HighQualityTextField"))
        windows.setParent(u = True)
        #Front
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_sideHighQualityTextField", l = "Profile", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_sideHighQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_sideHighQualityTextField"))
        windows.setParent(u = True)
        #Right 3/4
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_back34HighQualityTextField", l = "Back 3/4", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_back34HighQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_back34HighQualityTextField"))
        windows.setParent(u = True)
        #Right
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_backHighQualityTextField", l = "Back", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_backHighQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_backHighQualityTextField"))
        windows.setParent(u = True)
        
        windows.setParent(u = True)
        ####
        ####Right Frame
        ####
        windows.columnLayout()
        windows.text("Low Quality Images")

        #Front
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_frontLowQualityTextField", l = "Front", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_frontLowQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_frontLowQualityTextField"))
        windows.setParent(u = True)
        #Front 3/4
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_front34LowQualityTextField", l = "Front 3/4", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_front34LowQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_front34LowQualityTextField"))
        windows.setParent(u = True)
        #Side
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_sideLowQualityTextField", l = "Profile", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_sideLowQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_sideLowQualityTextField"))
        windows.setParent(u = True)
        #Back 3/4
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_back34LowQualityTextField", l = "Back 3/4", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_back34LowQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_back34LowQualityTextField"))
        windows.setParent(u = True)
        #Back
        windows.rowLayout(nc = 2)
        windows.textFieldGrp("oc_backLowQualityTextField", l = "Back", cw2 = (60,140), cc = lambda x: self.updateImagePlanePaths())
        windows.iconTextButton("oc_backLowQualityBrowseButton", style = "iconOnly", image1 = "menuIconFile.png", w = 30, h = 30, c = lambda: self.loadImage("oc_backLowQualityTextField"))
        windows.setParent(u = True)
        windows.setParent(u = True)
        
        windows.setParent(u = True)
        windows.setParent(u = True)
        
        
        ##-End body of UI
        windows.setParent(u = True)
        windows.showWindow("orthoCams")