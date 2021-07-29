from .SimpleQueue import SimpleQueue
from .Content import BaseExtender
import json
import time

class WorkImage():
    # Construct Methods
    def __init__(self, spiderControl: SimpleQueue, dataStorage: list, errorControl: SimpleQueue, errorInfo: SimpleQueue):
        self.spiderControl = spiderControl
        self.dataStorage = dataStorage
        self.errorControl = errorControl
        self.errorInfo = errorInfo
        return

    @classmethod
    def FromJson(cls, path: str):
        with open(path, "r", encoding = "utf8") as jsonFile:
            workImageDict = json.load(jsonFile)
        spiderControl = SimpleQueue.FromDict(workImageDict["SpiderControl"])
        dataStorage = workImageDict["DataStorage"]
        errorControl = SimpleQueue.FromDict(workImageDict["ErrorControl"])
        errorInfo = SimpleQueue.FromDict(workImageDict["ErrorInfo"])
        return cls(spiderControl, dataStorage, errorControl, errorInfo)

    @classmethod
    def FromDir(cls, path: str, storageLengthLimit: int):
        pass

    @classmethod
    def New(cls, initialItems: list):
        spiderControl = SimpleQueue()
        spiderControl.AddItems(initialItems)
        dataStorage = list()
        errorControl = SimpleQueue()
        errorInfo = SimpleQueue()
        return cls(spiderControl, dataStorage, errorControl, errorInfo)

    # Methods
    def Save(self, path: str):
        workImageDict = {
            "SpiderControl": self.spiderControl.AsDict,
            "DataStorage": self.dataStorage,
            "ErrorControl": self.errorControl.AsDict,
            "ErrorInfo": self.errorInfo.AsDict
        }
        with open(path, "w", encoding = "utf8") as jsonFile:
            json.dump(workImageDict, jsonFile, ensure_ascii = False, indent = 4)
        return
    
    def SaveAsDir(self, path: str, storageLengthLimit: int):
        pass

class SimpleSpiderFrame():
    # Construct Methods
    def __init__(self, NetWalker, Extender = BaseExtender, logFile = None):
        self.NetWalker, self.Extender, self.logFile = NetWalker, Extender, logFile
        return

    # Methods
    def LoadWorkImage(self, workImage: WorkImage):
        self.workImage = workImage
        return

    def NewStart(self, initialItems: list, outputPath: str, groupSize: int):
        self.LoadWorkImage(WorkImage.New(initialItems))
        self.StartSpider(outputPath, groupSize)
        return
        
    def Continue(
        self, outputPath: str, groupSize: int, workImage: WorkImage = None, 
        workImagePath: str = None, fixError: bool = True
    ):
        if not workImage == None:
            self.LoadWorkImage(workImage)
        elif not workImagePath == None:
            self.LoadWorkImage(WorkImage.FromJson(workImagePath))
        else:
            return
        if fixError:
            self.FixError()
        self.StartSpider(outputPath, groupSize)
        return

    def FixError(self):
        while not self.workImage.errorControl.IsEmpty:
            self.workImage.spiderControl.Add(
                self.workImage.errorControl.Pop()
            )
            self.workImage.errorInfo.Pop()
        return

    def StartSpider(self, outputPath: str, groupSize: int):
        numIndex = 1

        while not self.workImage.spiderControl.IsEmpty:
            if numIndex % groupSize == 0:
                self.ReportCache()
                self.workImage.Save(outputPath)
                self.ReportCacheSavingDone()

            self.ReportProcess()
            spiderItem = self.workImage.spiderControl.Pop()
            netWalker = self.NetWalker(spiderItem, self.logFile)
            isError, result = netWalker.Result
            if isError:
                self.workImage.errorControl.Add(spiderItem)
                self.workImage.errorInfo.Add(result)
            else:
                self.workImage.dataStorage.append(result[0])
                self.Extender(self.workImage.spiderControl, result[1])
            self.ReportResult(isError, result)

            self.SpiderPause()
            numIndex += 1

        self.ReportCache()
        self.workImage.Save(outputPath)
        self.ReportCacheSavingDone()
        return
        
    def ReportProcess(self):
        now = self.workImage.spiderControl.Head + 1
        total = self.workImage.spiderControl.Tail
        process = now / total * 100
        content = "Now: {}, Total: {}, Pseudo-Process: {:.2f}%.".format(now, total, process)
        print(content)
        if not self.logFile == None:
            self.logFile.write(content + "\n")
        return

    def ReportResult(self, isError: bool, result: str = ""):
        content = "Fail.\n{}\n".format(result) if isError else "Done.\n"
        print(content)
        if not self.logFile == None:
            self.logFile.write(content + "\n")
            self.logFile.flush()
        return

    def ReportCache(self):
        content = "Saving workimage...."
        print(content)
        if not self.logFile == None:
            self.logFile.write(content + "\n")
            self.logFile.flush()
        return

    def ReportCacheSavingDone(self):
        content = "Complete saving workimage.\n"
        print(content)
        if not self.logFile == None:
            self.logFile.write(content + "\n")
            self.logFile.flush()
        return

    def SpiderPause(self):
        time.sleep(1)
        return

class MultiThreadSpiderFrame():
    pass
