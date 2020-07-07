import numpy as np
from matplotlib import pyplot as plt
import pickle

version = "0.0.1"

class SimulationInterface():

    def __init__(self):
        """
        Initializes the class, with no parameters. 
        Will assume that if you have the colab library installed, 
        you're running on google colab(oratory). 
        """
        self.configuration = self.__get_configuration()
        self.parameters = {}
        self.data = {}
        self.simulation = {}
        return

    def __get_configuration(self):
        """
        .
        """
        # Gets the python environmnet
        try:
            import colab
            pyenv = "google_colab"
        except:
            try:
                aux = __file__
                pyenv = "python"
            except:
                print("Not in python")
                pyenv = "jupyter_notebook"
        print("Environment: ", pyenv)
        # Gets the library version
        simint = version
        # Pack and return
        configuration = {
                         "python_environment":pyenv,
                         "version":version,
                         }
        return configuration

    def new(self, parameters, data=None):
        self.parameters = parameters
        self.data = data
    
    def create_seed(self):
        filename = "my_simulation.sim"
        # pickle and return
        my_dict = {
                   "parameters":self.parameters, 
                   "simulation":self.simulation,
                   "data":self.data,
                  }
        with open(filename, "wb") as fh:
            pickle.dump(my_dict, fh)  
        return

    def create_from_seed(self):
        filename = "my_simulation.sim"
        # Unpack and assign
        with open(filename, "rb") as f:
            my_dict = pickle.load(f)
        self.parameters = my_dict["parameters"] 
        self.simulation = my_dict["simulation"] 
        self.data = my_dict["data"] 
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
       self.simulation = {"x":x, "y":y}
       return
    
    def plot(self):
        x = self.simulation["x"]
        y = self.simulation["y"]
        data = self.data
        plt.figure(figsize=(16,8))
        plt.plot(x, y, "-", label="sim")
        plt.plot(data["x"], data["y"], "o", label="data")
        plt.show()
        return

    def download(self, extension):
        if extension=="seed":
            print("Creating a seed")
            self.create_seed()
            if self.configuration["python_environment"]=="google_colab":
                from google.colab import files
                files.download("my_simulation.sim")
            else:
                print("Not downloading")

        elif extension=="xlsx":
            self.__export_xlsx()
        return

    def __export_xlsx(self):
        print("creating xlsx")
        filename = "test.xlsx"
        # Create the file
        with open(filename, "w") as fh:
            fh.write("Este es un test\n")
            fh.write("TEST")
        # Download the file
        if self.configuration["python_environment"]=="google_colab":
            from google.colab import files
            files.download(filename)
        return
        
        