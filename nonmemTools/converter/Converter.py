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
        pathRltDir  = os.path.join(self.config.getStateValue("dirPath"),"convertedCSV")
        os.makedirs(pathRltDir, exist_ok=True)
        
        for eachCSV in csvFileList :
            timeLine    = None
            wholeData   = list()
            pathEachCSV = os.path.join(self.config.getStateValue("dirPath"),"csvForms",eachCSV)
            pathRltCSV  = os.path.join(pathRltDir,"converted_"+eachCSV)

            with open(pathEachCSV,"r") as csvStream :
                reader = csv.reader(csvStream)
                for index, each in enumerate(reader,start=0) :
                    if index==0 : 
                        timeLine = each[1:]
                        continue
                    else : wholeData.append(each[2:])

                
            with open(pathRltCSV,"w",encoding="utf-8") as csvStream :
                writer = csv.writer(csvStream)
                writer.writerow(["ID","TIME","DV","MDV"])

                for numID,eachAgent in enumerate(wholeData,start=1) :
                    for i, eachData in enumerate(eachAgent,start=0) :
                        if eachData == "BQL" : eachData = "."
                        if eachData == "-" : continue
                        eachLine = [numID]              # ID
                        eachLine.append(timeLine[i])    # TIME
                        eachLine.append(eachData)       # DV
                        if i == 0 : eachLine.append(1)  # MDV
                        else : eachLine.append(0)
                        writer.writerow(eachLine)



        



if __name__ == "__main__" :
    converter = Converter()
    converter.initContainer()
    converter.convertCSV()


