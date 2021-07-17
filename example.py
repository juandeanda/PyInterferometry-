from pyInterferometry.read import *
from pyInterferometry.CreateInterferogram import *

coefficients, degree = read("Coefficients.json")
numCoef = readNumericalCoef(coefficients,degree)
Interferogram = Interferogram()
Interferogram.genInterferogramMonomial(numCoef)


