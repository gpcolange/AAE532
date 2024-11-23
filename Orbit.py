import numpy as np
import matplotlib.pyplot as plt

class orbit: 
    def __init__(self,a,e):
        self.a      = a
        self.e      = e
        self.p      = self.a*(1 - self.e**2)
        self.rp     = a*(1 - e)
        self.ra     = a*(1 + e)

    def OrbitProps(self,mu, r = None):
        self.h      = np.sqrt(mu*self.p)
        self.energy = -mu/(2*self.a)

        if r is None:
            pass
        else: 
            self.v              = np.sqrt(2*(self.energy + mu/r))

    def PlotOrbit(self):
        # x   = []
        # y   = []
        # for ta in np.arange(0,2*np.pi,.01):
        #     r = self.p/(1 + self.e*np.cos(ta))
        #     x.append(r*np.cos(ta))
        #     y.append(r*np.sin(ta))

        ta_vec  = np.arange(0,2*np.pi,.01)
        x_vec   = (self.p/(1 + self.e*np.cos(ta_vec)))*np.cos(ta_vec)
        y_vec   = (self.p/(1 + self.e*np.cos(ta_vec)))*np.sin(ta_vec)

        plt.plot(x_vec, y_vec)
        plt.xlabel("X")
        plt.ylabel("Y ")
        plt.title("Orbit")
        plt.axis('equal')
        plt.show()



a = 5*6378.1363
e = 0.8

o1 = orbit(a,e)
o1.OrbitProps(398600.4415,o1.ra)
print(o1.v)
o1.PlotOrbit()

