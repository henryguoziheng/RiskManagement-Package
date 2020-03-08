import copy
import numpy as np
import pandas as pd
from GeneralModel import GeneralModel


class NumericalModel(GeneralModel):
    '''
    Use numerical method to get values of different risk measures
    '''
    def __init__(self):
        super().__init__()
        self.LossDist = self.LossDist()
        self.pmf = self.pmf()

    class LossDist():

        def __init__(self):
            pass

        def getVaR(self, alpha, pnl):
            return pnl.quantile(alpha, interpolation='higher')

        def getExpectedShortfall(self, alpha, pnl):
            if isinstance(alpha, float):
                tempVaR = self.getVaR(alpha, pnl)
                return pnl[pnl.ge(tempVaR)].mean()

            if type(alpha) is np.ndarray:
                ES = []
                for tempAlpha in alpha:
                    tempVaR = self.getVaR(tempAlpha, pnl)
                    tempES = pnl[pnl.ge(tempVaR)].mean()
                    ES.append(tempES)
                return pd.Series(ES)

    class pmf():

        def __init__(self):
            pass

        def getVaR(self, alpha, pmf):
            temp = copy.deepcopy(pmf)
            temp['Probabilities'] = temp['Probabilities'].cumsum()
            return temp['P&L'][temp['Probabilities'].ge(alpha).idxmax()]

        def getExpectedShortfall(self, alpha, pmf):
            temp1 = copy.deepcopy(pmf)
            temp1['Probabilities'] = temp1['Probabilities'].cumsum()
            startPoint = temp1['Probabilities'].ge(alpha).idxmax()
            pmf = pmf.iloc[startPoint:]
            pmf['temp'] = pmf.apply(lambda x: x['Probabilities'] * x['P&L'], axis=1)
            return np.sum(pmf['temp']) / (1-alpha)



