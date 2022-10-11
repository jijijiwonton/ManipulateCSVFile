import pytest
from controller import Controller
from model import Model
from view import View

def test_addNewRecord():
    model = Model("source", "latin", "english", "french", "year", "month", "number")
    view = View()
    
    controller = Controller(model, view)
    controller.runCreateNewRecord(Model("newSource", "newLatin", "newEnglish", "newFrench", "newYear", "newMonth", "newNumber"))
    assert 101 == len(controller.inMemoryData)