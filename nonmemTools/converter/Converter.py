import csv
import os
import json
import sys

class Converter  :
    def __init__(self) :
        pathDir = os.path.dirname(os.path.abspath(__file__))
        pathModule = os.path.join(pathDir,"..","..")
        sys.path.append(pathModule)
        import Configurator
        self.config = Configurator.Configurator()
        os.chdir(pathDir)
        self.config.setStateValue("dirPath",pathDir)

    def initContainer(self) :
        csvFileList = os.listdir("csvForms")
        self.config.setStateValue("csvFileList",csvFileList)
    
    def convertCSV(self) :
        csvFileList = self.config.getStateValue("csvFileList")
        for eachCSV in csvFileList :
            pathEachCSV = os.path.join(self.config.getStateValue("dirPath"),eachCSV)
            wholeLine = None
            with open(pathEachCSV,"r") as csvStream :
                wholeLine = 



if __name__ == "__main__" :
    converter = Converter()
    converter.initContainer()
    converter.convertCSV()


