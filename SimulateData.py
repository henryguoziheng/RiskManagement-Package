from scipy import stats
import pandas as pd
from DataController import DataController

class SimulateData(DataController):
    '''
    class to generate loss distribution by simulating data
    method :: MonteCarlo, get loss distribution by Monte Carlo Simulation
    method :: Classical, get loss distribution by classical distributions e.g. Gaussian, Student-t
    '''
    def __init__(self):
        super().__init__()
        self.classical = self.Classical()
        self.montecarlo = self.MonteCarlo()

    class MonteCarlo(object):

        def __init__(self):
            pass

    class Classical(object):
        def __init__(self):
            pass

        def normal(self, mean, variance, size):
            lossDist  = stats.norm.rvs(mean, variance, size)
            return pd.Series(lossDist)

        def t(self, niu, size):
            '''
            :param niu: degree of freedom
            :return:
            '''
            lossDist = stats.t.rvs(niu, size = size)
            return pd.Series(lossDist)

        def binomial(self, n, p, size):
            lossDist = stats.binom.rvs(n, p, size=size)
            return pd.Series(lossDist)
