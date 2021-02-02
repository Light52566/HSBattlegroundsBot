import json

class CardLibrary:
    def __init__(self, libpath):
        self.libpath = libpath
        self.cardlib = None

    def __init__(self):
        self.libpath = None
        self.cardlib = None

    def setPath(self, libpath):
        self.libpath = libpath
    
    def loadLibrary(self):
        try:
            fp = open(self.libpath, 'r')
            self.cardlib = json.load(fp)
            fp.close()
        except:
            print("Card Library json not found at", self.libpath)
        
        
    
    def getLibrary(self):
        return self.cardlib
        