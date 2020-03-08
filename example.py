
import numpy as np
import RiskManagement as rm

# Instantiation from controller class
controller = rm.dataController()
# Read local data (for online data, use .downLoadData(tickerList,beginDate, endDate))
url = 'http://math.iit.edu/~igor/LN/Math588/TestDataProject1.xlsx'
excel = controller.readLocalData(url, sheetName='Sheet1')
# Choose the risk factor we want from raw data, here we use adjusted close
riskFactor = controller.getRiskFactor('Adj Close')
# Apply deterministic function to risk factor to get loss distribution
lossDist = controller.getlossDist(lambda x: np.log(x))

# Instantiation from model class
model = rm.numericalModel()
# Use loss distribution to calculate value at risk
alpha = 0.95
VaR = model.LossDist.getVaR(alpha, lossDist)




