from ExplicitModel import ExplicitModel
from DataController import DataController
from GeneralController import GeneralController
from GeneralModel import GeneralModel
from NumericalModel import NumericalModel
from SimulateData import SimulateData

# class explicitModel(ExplicitModel):
#     def __init__(self):
#         super().__init__()

def explicitModel(*args, **kwargs):
    return ExplicitModel()

def dataController(*args, **kwargs):
    return DataController()

def numericalModel(*args, **kwargs):
    return NumericalModel()

def simulateData(*args, **kwargs):
    return SimulateData()