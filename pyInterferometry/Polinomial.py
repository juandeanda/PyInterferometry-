import math
def Zernike(x,y,coef):
     switcher={
         0: 1+0*x+0*y,
         1: 2*x+0*y,
         2: 2*y+0*x,
         3: math.sqrt(3)*((2*rho2(x,y))-1),
         4: math.sqrt(6)*(2*x*y),
         5: math.sqrt(6)*(x*x-y*y),
         6: math.sqrt(8)*(y*((3*rho2(x,y))-2)),
         7: math.sqrt(8)*(x*((3*rho2(x,y))-2)),
         8: math.sqrt(8)*(y*((3*x*x)-y*y)),
         9: math.sqrt(8)*(x*(x*x-(3*y*y))),
         10: math.sqrt(5)*((6*rho4(x,y))-(6*rho2(x,y))+1),
         11: math.sqrt(10)*((x*x-y*y)*((4*rho2(x,y))-3)),
         12: math.sqrt(10)*((2*x*y)*((4*rho2(x,y))-3)),
         13: math.sqrt(10)*(rho4(x,y)-(8*x*x*y*y)),
         14: math.sqrt(10)*((4*x*y)*(x*x-y*y)),
         15: math.sqrt(12)*(x*((10*rho4(x,y))-(12*rho2(x,y))+3)),
         16: math.sqrt(12)*(y*((10*rho4(x,y))-(12*rho2(x,y))+3)),
         17: math.sqrt(12)*(x*(x*x-(3*y*y))*((5*rho2(x,y))-4)),
         18: math.sqrt(12)*(y*((3*x*x)-y*y)*((5*rho2(x,y))-4)),
         19: math.sqrt(12)*(x*((16*x*x*x*x)-(20*x*x*rho2(x,y))+(5*rho4(x,y)))),
         20: math.sqrt(12)*(y*((16*y*y*y*y)-(20*y*y*rho2(x,y))+(5*rho4(x,y)))),
         21: math.sqrt(7)*(((20*rho6(x,y))-(30*rho4(x,y))+(12*rho2(x,y))-1)),
         22: math.sqrt(14)*((2*x*y)*((15*rho4(x,y))-(20*rho2(x,y))+6)),
         23: math.sqrt(14)*((x*x-y*y)*((15*rho4(x,y))-(20*rho2(x,y))+6)),
         24: math.sqrt(14)*((4*x*y)*(x*x-y*y)*((6*rho2(x,y))-5)),
         25: math.sqrt(14)*(((8*x*x*x*x)-(8*x*x*rho2(x,y))+(rho4(x,y)))*((6*rho2(x,y))-5)),
         26: math.sqrt(14)*((x*y)*((32*x*x*x*x)-(32*x*x*x*rho2(x,y))+(6*rho4(x,y)))),
         27: math.sqrt(14)*((32*x*x*x*x*x*x)-(48*x*x*x*x*rho2(x,y))+(18*x*x*rho4(x,y))-rho6(x,y))
     }
     return switcher.get(coef,"Invalid")
     
def Monomial(x,y,coef):
     switcher={
         0: 1+0*x+0*y,
         1: 2*x+0*y,
         2: 2*y+0*x,
         3: x**2,
         4: x*y,
         5: y*2,
         6: x**3,
         7: x**2*y,
         8: x*y**2,
         9: y**3,
         10: x**4,
         11: x**3*y,
         12: x**2*y**2,
         13: x*y**3,
         14: y**4,
         15: x**5,
         16: x**4*y,
         17: x**3*y**2,
         18: x**2*y**3,
         19: x*y**4,
         20: y**5,
         21: x**6,
         22: x**5*y,
         23: x**4*y**2,
         24: x**3*y**3,
         25: x**2*y**4,
         26: x*y**5,
         27: y**6
     }
     return switcher.get(coef,"Invalid") 
def rho2(x,y):
    x2 = x*x
    y2 = y*y
    return x2+y2
def rho4(x,y):
    r2 = rho2(x,y)
    return  r2*r2
def rho6(x,y):
    r2 =  rho2(x,y)
    return r2*r2*r2       



