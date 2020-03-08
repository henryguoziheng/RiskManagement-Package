import pandas as pd
import numpy as np
import pandas_datareader as pdr
from GeneralController import GeneralController


class DataController(GeneralController):

    def __init__(self):

        super().__init__()
        self.localCalled = False
        self.loadCalled = False
        # self.localData = None
        # self.loadData = None
        # self.riskFactorData = pd.DataFrame()

    def readLocalData(self, url, sheetName=None, rowRange=None, columnRange=None):
        self.localData = pd.read_excel(url, sheet_name=sheetName,usecols=columnRange ,nrows=rowRange)
        self.localCalled = True
        return self.localData

    def downLoadData(self, tickerList,beginDate, endDate):
        self.loadData = pdr.get_data_yahoo(tickerList, beginDate, endDate)
        self.loadCalled = True
        return self.loadData

    def getRiskFactor(self, riskFactor):

        if self.localCalled == True:
            self.riskFactorData = self.localData[riskFactor]
        if self.loadCalled == True:
            self.riskFactorData = self.loadData[riskFactor]

        return self.riskFactorData

    def getlossDist(self, deterministicFunction):
        lossDist = -self.riskFactorData.apply(deterministicFunction).diff().dropna()
        return lossDist
