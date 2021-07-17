import numpy as np
import matplotlib.pyplot as plt
from pyInterferometry.Polinomial import Zernike, Monomial
class Interferogram:
    def __init__(self,width=512,high=512,x_i=-1,x_f=1,y_i=-1,y_f=1):
        self.width = width
        self.high = high 
        self.x_i = x_i
        self.x_f = x_f
        self.y_i = y_i
        self.y_f = y_f

    def phi_Zernike(self,x,y,coef,i=0):
       if len(coef)==1:
         return coef[0]
       return coef[0]*Zernike(x,y,i)+phi_Zernike(x,y,coef[1:],i+1)

    def phi_Monomial(self,x,y,coef,i=0):
       if len(coef)==1:
         return coef[0]
       return coef[0]*Monomial(x,y,i)+self.phi_Monomial(x,y,coef[1:],i+1)

    def genInterferogramMonomial(self,coef):
        x = np.arange(self.x_i,self.x_f, 0.1)
        y = np.arange(self.y_i, self.y_f, 0.1)
        xx, yy = np.meshgrid(x, y, sparse=True)
        z = np.cos(self.phi_Monomial(xx,yy,coef))
        h = plt.contourf(x, y, z)
        plt.axis('scaled')
        plt.show()
