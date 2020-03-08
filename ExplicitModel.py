from scipy import stats
import numpy as np

class ExplicitModel():

    def __init__(self):
        self.VALID_DISTRIBUTION = {'Normal', 'Student-t', 'Multi-Normal'}

    def getVaR(self, alpha, distribution, mean=0, std=1, df=2):
        if distribution not in self.VALID_DISTRIBUTION:
            raise ValueError("Distribution must be one of %r." % self.VALID_DISTRIBUTION)

        else:
            if distribution == 'Normal':
                VaR = stats.norm(mean, std).ppf(alpha)
                return VaR
            if distribution == 'Student-t':
                VaR = stats.t(df, mean, std).ppf(alpha)
                return VaR


    def getES(self, alpha, distribution, mean=0, std=1, df=2):
        if distribution not in self.VALID_DISTRIBUTION:
            raise ValueError("Distribution must be one of %r." % self.VALID_DISTRIBUTION)

        else:
            if distribution == 'Normal':
                Z = (1/(1-alpha))*(stats.norm.pdf(stats.norm.ppf(alpha)))
                return mean + std*Z

            if distribution =='Student-t':
                Z = (stats.t(df, mean, std).pdf(stats.t(df, mean, std).ppf(alpha)) * (df + np.power(stats.t(df, mean, std).ppf(alpha),2)))/((1-alpha)*(df-1))
                return mean + std*Z


    def getMultiNormVaR(self, alpha, distribution, mean, covMat, Taylor):
        '''
        :param alpha: float
        :param distribution: str, 'Multi-Normal'
        :param mean: vector
        :param covMat: matrix
        :param Taylor: list, contains the first and second term in Taylor Series; namely ct and bt in the project
        :return: float, value at risk
        '''
        if distribution not in self.VALID_DISTRIBUTION:
            raise ValueError("Distribution must be one of %r." % self.VALID_DISTRIBUTION)
        else:
            if distribution == 'Multi-Normal':
                miu = -(Taylor[0] + np.dot(Taylor[1], mean))
                var = np.dot(Taylor[1], np.dot(covMat, Taylor[1]))
                return stats.norm(miu, var).ppf(alpha)

    def getMultiNormES(self, alpha, distribution, mean, covMat, Taylor):
        if distribution not in self.VALID_DISTRIBUTION:
            raise ValueError("Distribution must be one of %r." % self.VALID_DISTRIBUTION)

        else:
            if distribution == 'Multi-Normal':
                miu = -(Taylor[0] + np.dot(Taylor[1], mean))
                std = np.dot(Taylor[1], np.dot(covMat, Taylor[1]))
                Z = (1 / (1 - alpha)) * (stats.norm.pdf(stats.norm.ppf(alpha)))
                return miu + std*Z
