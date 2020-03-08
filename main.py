import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import RiskManagement as rm


#=================================================================================
#
# Problem 1
#
# url = 'http://math.iit.edu/~igor/LN/Math588/TestDataProject1.xlsx'
# excel = rm.dataController().readLocalData(url, sheetName='Sheet1')
# print (excel)
#==================================================================================
#
# Problem 2.a, 3.a
#
# url = 'http://math.iit.edu/~igor/LN/Math588/TestDataProject1.xlsx'
# excel = rm.dataController().readLocalData(url, sheetName='Sheet2')
#
# alpha = 0.95
#
# VaR = rm.numericalModel().pmf.getVaR(alpha, pmf=excel)
# ES = rm.numericalModel().pmf.getExpectedShortfall(alpha, pmf=excel)
#
# print ('Value at Risk given pmf: {}'.format(VaR))
# print ('Expected Shortfall given pmf: {}'.format(ES))

#===================================================================================
#
# Problem 2.b, 3.b
#
# url = 'http://math.iit.edu/~igor/LN/Math588/TestDataProject1.xlsx'
# excel = rm.dataController()
# excel.readLocalData(url, sheetName = 'Sheet1')
# excel.getRiskFactor('Adj Close')
# pnl = excel.getlossDist(lambda x: np.log(x))
#
# alpha = 0.95
# model = rm.numericalModel()
# VaR = model.LossDist.getVaR(alpha, pnl)
# ES = model.LossDist.getExpectedShortfall(alpha, pnl)
#
# print ('Value at Risk given Loss Distribution: {}'.format(VaR))
# print ('Expected Shortfall given Loss Distribution: {}'.format(ES))
#
#==================================================================================
#
# Problem 2.c, 3.c
#
# alpha = 0.99
# model = rm.explicitModel()
#
# VaR_norm = model.getVaR(alpha, 'Normal')
# ES_norm = model.getES(alpha, 'Normal')
#
# VaR_t = model.getVaR(alpha, 'Student-t')
# ES_t = model.getES(alpha, 'Student-t')
#
# print ('Value at Risk under Normal Dist: {}'.format(VaR_norm))
# print ('Expected Shortfall under Normal Dist: {}'.format(ES_norm))
# print ('Value at Risk under t Dist: {}'.format(VaR_t))
# print ('Expected Shortfall under t Dist: {}'.format(ES_t))
#
#=================================================================================
#
#Problem 4
#
# pnl = rm.simulateData().classical.t(4, 10000)
# alpha = np.linspace(0.5, 1, 300)
#
# model = rm.numericalModel()
#
# VaR = model.LossDist.getVaR(alpha, pnl)
# ES = model.LossDist.getExpectedShortfall(alpha, pnl)
#
# sns.set()
# plt.plot(alpha, VaR, 'r', label='VaR')
# plt.plot(alpha, ES, 'b', label='ES')
# plt.ylim((0, 10))
# plt.title('VaR & ES given different alpha (t Distribution)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
# plt.show()
#
#=====================================================================================
#
# Problem 6 VaR
#
# Lt1 = rm.simulateData().classical.t(4, 1000)
# Lt2 = rm.simulateData().classical.t(4, 1000)
#
# Ln1 = rm.simulateData().classical.normal(0, 1, 1000)
# Ln2 = rm.simulateData().classical.normal(0, 1, 1000)
#
# Lb1 = rm.simulateData().classical.binomial(100, 0.1, 1000)
# Lb2 = rm.simulateData().classical.binomial(100, 0.1, 1000)
#
# Lb3 = rm.simulateData().classical.binomial(10, 0.01, 1000)
# Lb4 = rm.simulateData().classical.binomial(10, 0.01, 1000)
#
# alpha = np.linspace(0.5, 1, 300)
#
# model = rm.numericalModel()
#
# VaRLt1 = model.LossDist.getVaR(alpha, Lt1)
# VaRLt2 = model.LossDist.getVaR(alpha, Lt2)
# VaRLtsum = model.LossDist.getVaR(alpha, Lt1+Lt2)
#
# VaRLn1 = model.LossDist.getVaR(alpha, Ln1)
# VaRLn2 = model.LossDist.getVaR(alpha, Ln2)
# VaRLnsum = model.LossDist.getVaR(alpha, Ln1+Ln2)
#
# VaRLb1 = model.LossDist.getVaR(alpha, Lb1)
# VaRLb2 = model.LossDist.getVaR(alpha, Lb2)
# VaRLbsum = model.LossDist.getVaR(alpha, Lb1+Lb2)
#
# VaRLb3 = model.LossDist.getVaR(alpha, Lb3)
# VaRLb4 = model.LossDist.getVaR(alpha, Lb4)
# VaRLbsum4 = model.LossDist.getVaR(alpha, Lb3+Lb4)
#
# sns.set()
# plt.figure()
# plt.subplot(2,2,1)
# plt.plot(alpha, VaRLt1+VaRLt2, 'r', label='VaR(X) + VaR(Y)')
# plt.plot(alpha, VaRLtsum, 'b', label='VaR(X+Y)')
# plt.title('Subadditivity of VaR (t)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,2)
# plt.plot(alpha, VaRLn1+VaRLn2, 'r', label='VaR(X) + VaR(Y)')
# plt.plot(alpha, VaRLnsum, 'b', label='VaR(X+Y)')
# plt.title('Subadditivity of VaR (Normal)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,3)
# plt.plot(alpha, VaRLb1+VaRLb2, 'r', label='VaR(X) + VaR(Y)')
# plt.plot(alpha, VaRLbsum, 'b', label='VaR(X+Y)')
# plt.title('Subadditivity of VaR (Binomial)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,4)
# plt.plot(alpha, VaRLb3+VaRLb4, 'r', label='VaR(X) + VaR(Y)')
# plt.plot(alpha, VaRLbsum4, 'b', label='VaR(X+Y)')
# plt.title('Subadditivity of VaR (Binomial)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.show()
#
#======================================================================================
#
# Problem 6 ES
#
# Lt1 = rm.simulateData().classical.t(4, 1000)
# Lt2 = rm.simulateData().classical.t(4, 1000)
#
# Ln1 = rm.simulateData().classical.normal(0, 1, 1000)
# Ln2 = rm.simulateData().classical.normal(0, 1, 1000)
#
# Lb1 = rm.simulateData().classical.binomial(100, 0.2, 1000)
# Lb2 = rm.simulateData().classical.binomial(100, 0.2, 1000)
#
# Lb3 = rm.simulateData().classical.binomial(50, 0.1, 1000)
# Lb4 = rm.simulateData().classical.binomial(50, 0.1, 1000)
#
# alpha = np.linspace(0.5, 1, 300)
#
# model = rm.numericalModel()
#
# VaRLt1 = model.LossDist.getExpectedShortfall(alpha, Lt1)
# VaRLt2 = model.LossDist.getExpectedShortfall(alpha, Lt2)
# VaRLtsum = model.LossDist.getExpectedShortfall(alpha, Lt1+Lt2)
#
# VaRLn1 = model.LossDist.getExpectedShortfall(alpha, Ln1)
# VaRLn2 = model.LossDist.getExpectedShortfall(alpha, Ln2)
# VaRLnsum = model.LossDist.getExpectedShortfall(alpha, Ln1+Ln2)
#
# VaRLb1 = model.LossDist.getExpectedShortfall(alpha, Lb1)
# VaRLb2 = model.LossDist.getExpectedShortfall(alpha, Lb2)
# VaRLbsum = model.LossDist.getExpectedShortfall(alpha, Lb1+Lb2)
#
# VaRLb3 = model.LossDist.getExpectedShortfall(alpha, Lb3)
# VaRLb4 = model.LossDist.getExpectedShortfall(alpha, Lb4)
# VaRLbsum4 = model.LossDist.getExpectedShortfall(alpha, Lb3+Lb4)
#
# sns.set()
# plt.figure()
# plt.subplot(2,2,1)
# plt.plot(alpha, VaRLt1+VaRLt2, 'r', label='ES(X) + ES(Y)')
# plt.plot(alpha, VaRLtsum, 'b', label='ES(X+Y)')
# plt.title('Subadditivity of ES (t)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,2)
# plt.plot(alpha, VaRLn1+VaRLn2, 'r', label='ES(X) + ES(Y)')
# plt.plot(alpha, VaRLnsum, 'b', label='ES(X+Y)')
# plt.title('Subadditivity of ES (Normal)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,3)
# plt.plot(alpha, VaRLb1+VaRLb2, 'r', label='ES(X) + ES(Y)')
# plt.plot(alpha, VaRLbsum, 'b', label='ES(X+Y)')
# plt.title('Subadditivity of ES (Binomial)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.subplot(2,2,4)
# plt.plot(alpha, VaRLb3+VaRLb4, 'r', label='ES(X) + ES(Y)')
# plt.plot(alpha, VaRLbsum4, 'b', label='ES(X+Y)')
# plt.title('Subadditivity of ES (Binomial)')
# plt.legend()
# plt.xlabel('Alpha')
# plt.ylabel('Amount of Risk')
#
# plt.show()
