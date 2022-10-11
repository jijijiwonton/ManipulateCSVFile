from model import Model
from view import View
from controller import Controller

class Main:
    model = Model("Source", "latin", "english", "french", "year", "month", "number")
    view = View()
    
    controller = Controller(model, view)

    controller.runReloadData()
    controller.createNewFile()
    controller.runOneRecord(0)
    controller.runCreateNewRecord(Model("newSource", "newLatin", "newEnglish", "newFrench", "newYear", "newMonth", "newNumber"))
    controller.runEditRecord(0, ["editSource", "editLatin", "editEnglish", "editFrench", "editYear", "editMonth", "editNumber"])
    controller.runOneRecord(0)
    controller.runDeleteRecord(1)
    controller.runReloadData()
