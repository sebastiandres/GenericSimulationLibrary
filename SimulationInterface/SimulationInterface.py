import numpy as np
from matplotlib import pyplot as plt

class SimulationInterface():

    def __init__(self):
        return

    def new(self, parameters, data=None):
        self.parameters = parameters
        self.data = data
    
    def create_from_seed(self, seed):
        # Unpack and assign
        return

    def create_seed():
        # pickle and return
        return

    def simulate(self):
       # Unpack required values
       x_min = self.parameters["x_min"]
       x_max = self.parameters["x_max"]
       x_Npoints = self.parameters["x_Npoints"]
       m = self.parameters["m"]
       b = self.parameters["b"]
       x = np.linspace(x_min, x_max, num=x_Npoints)
       y = m*x + b
       self.x = x
       self.y = y
    
    def plot(self):
        x = self.x
        y = self.y
        data = self.data
        plt.figure(figsize=(16,8))
        plt.plot(x, y, "-", label="sim")
        plt.plot(data["x"], data["y"], "o", label="data")
        plt.show()

    def __export_doc(self):
        with open("test.doc", "w") as fh:
            fh.write("Este es un test\n")
            fh.write("TEST")

    def __export_xlsx(self):
        with open("test.xlsx", "w") as fh:
            fh.write("Este es un test\n")
            fh.write("TEST")
        
    def export(self, extension):
        if extension=="doc":
            self.__export_doc()
        elif extension=="xlsx":
            self.__export_doc()