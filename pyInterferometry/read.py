import json
import numpy as np

def read(file):
    #Reading of coefficients and degree of the interferogram 
    f = open(file)
    Parameters = json.load(f)
    coefficients = Parameters["Coefficients"]
    degree = Parameters["degree"]
    f.close()
    return coefficients, degree
def readNumericalCoef(coef,degree):
    Coefs = np.zeros(degree+1)
    for i in range(0,degree+1):
       a = "a_"+str(i)
       Coefs[i] = coef[0][a]
    return Coefs
