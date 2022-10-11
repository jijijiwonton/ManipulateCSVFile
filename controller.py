class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.inMemoryData = self.model.reloadData()
    
    def runReloadData(self):
        self.view.displayReloadData(self.inMemoryData)
        
    def createNewFile(self):
        newFileCreated = self.model.writeNewFileWithCommaSeparated("new_file.csv")
        self.view.confirmCreateNewFile(newFileCreated)
    
    def runOneRecord(self, indexNumber):
        self.view.displayOneView(indexNumber, self.inMemoryData)

    def runCreateNewRecord(self, newRecord):
        self.model.createNewRecord(self.inMemoryData, newRecord)
    
    def runEditRecord(self, indexNumber, values=[]):
        self.model.editRecord(indexNumber, self.inMemoryData, values)
        
    def runDeleteRecord(self, indexNumber):
        self.model.deleteOneRecord(indexNumber, self.inMemoryData)