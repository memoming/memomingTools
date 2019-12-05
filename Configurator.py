import json

class Configurator :
    def __init__(self) :
        self.config = dict()

    def setStateValue(self,key,value) :
        self.config[key] = value
    
    def getStateValue(self,key) :
        returnValue = None
        if key in self.config.keys() :
            returnValue = self.config[key]
        return returnValue