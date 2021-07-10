from pyInterferometry.read import *

coefficients, degree = read("Coefficients.json")
numCoef = readNumericalCoef(coefficients,degree)
