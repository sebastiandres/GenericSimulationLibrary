
import pickle
import sys
import time

from .version import __version__ as GSL_version

class SimulationInterface():
    """This is a conceptual class representation of a simple BLE device
    (GATT Server). It is essentially an extended combination of the
    :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

    :param client: A handle to the :class:`simpleble.SimpleBleClient` client
        object that detected the device
    :type client: class:`simpleble.SimpleBleClient`
    :param addr: Device MAC address, defaults to None
    :type addr: str, optional
    :param addrType: Device address type - one of ADDR_TYPE_PUBLIC or
        ADDR_TYPE_RANDOM, defaults to ADDR_TYPE_PUBLIC
    :type addrType: str, optional
    :param iface: Bluetooth interface number (0 = /dev/hci0) used for the
        connection, defaults to 0
    :type iface: int, optional
    :param data: A list of tuples (adtype, description, value) containing the
        AD type code, human-readable description and value for all available
        advertising data items, defaults to None
    :type data: list, optional
    :param rssi: Received Signal Strength Indication for the last received
        broadcast from the device. This is an integer value measured in dB,
        where 0 dB is the maximum (theoretical) signal strength, and more
        negative numbers indicate a weaker signal, defaults to 0
    :type rssi: int, optional
    :param connectable: `True` if the device supports connections, and `False`
        otherwise (typically used for advertising ‘beacons’).,
        defaults to `False`
    :type connectable: bool, optional
    :param updateCount: Integer count of the number of advertising packets
        received from the device so far, defaults to 0
    :type updateCount: int, optional
    """

    def __init__(self):
        """
        Initializes the class, with no inputs. 
        Will assume that if you have the colab library installed, 
        you're running on google colab(oratory). 
        """
        self.configuration = self.__get_configuration()
        self.inputs = {}
        self.data = {}
        self.outputs = {}
        return

    def __get_configuration(self):
        """Carefully tries to import required libraries,
        storing the python and library version.
        :return: Nothing
        :rtype: Nothing
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
        # Check the version for python
        try:
            import platform
            python_version = platform.python_version()
        except:
            python_version = ""
        # Check the version for numpy library
        try:
            from numpy import version as numpy_version
            numpy_version = numpy_version.version
        except:
            numpy_version = ""
        # Check the version for matplotlib pyplot
        try:
            from matplotlib import __version__ as plt_version
        except:
            plt_version = ""
        # Pack and return
        configuration = {
                         "environment":pyenv,
                         "python_version":python_version,
                         "GenericSimulationLibrary_version":GSL_version,
                         "numpy_version":numpy_version,
                         "matplotlib_version":plt_version,
                         }
        return configuration

    def status(self):
        """
        Prints the environment, python and library versions.
        """
        # Configuration
        print("System configuration:")
        for key in self.configuration:
            library = "    " + key.replace("_", " ") + ":"
            if self.configuration[key]:
                print(library, self.configuration[key])
            else:
                print(library, "Not installed")
        # Inputs
        print("Inputs:")
        if self.inputs:
            for key in self.inputs:
                print("    "+key, self.inputs[key])
        else:
            print("    No inputs")
        # Data
        print("Data:")
        if self.data:
            for key in self.data:
                print("    "+key, self.data[key])
        else:
            print("    No data")
        return 

    def new(self, inputs, data=None):
        """Associates inputs and plot options to the simulation. 

        :param inputs: The inputs that will be used in the simulation. 
        This can be completely personalized. 
        :type inputs: dict
        :param data: The plot options, defaults to None
        :type data: dict, optional
        """
        self.inputs = inputs
        self.data = data

    def save(self):
        """ My summary
        """
        if self.inputs and self.inputs["filename"]:
            filename = self.inputs["filename"]
        else:
            print("Cannot save the simulation. Filename was not defined.")
            return
        # pickle and return
        my_dict = {
                   "configuration":self.configuration,
                   "inputs":self.inputs, 
                   "outputs":self.outputs,
                   "data":self.data,
                  }
        with open(filename, "wb") as fh:
            pickle.dump(my_dict, fh)
            print("Saving simulation into file ", filename)
        if self.configuration["environment"]=="google_colab":
            from google.colab import files
            files.download(filename)
        return

    def load(self, filepath):
        # Unpack and assign
        with open(filepath, "rb") as f:
            my_dict=pickle.load(f)
        self.configuration=my_dict["configuration"]
        self.inputs=my_dict["inputs"] 
        self.outputs=my_dict["outputs"] 
        self.data=my_dict["data"]
        return

    def simulate(self):
        """
        Conditionally imports the numpy library.
        """
        if self.configuration["numpy_version"]:
            import numpy as np
        else:
            print("Cannot simulate - numpy library not installed.")
            return
        # Unpack required values
        x_min = self.inputs["x_min"]
        x_max = self.inputs["x_max"]
        N_points = self.inputs["N_points"]
        m = self.inputs["m"]
        b = self.inputs["b"]
        x = np.linspace(x_min, x_max, num=N_points)
        # Simulation
        for t in range(1,13):
            time.sleep(0.25)
            sys.stdout.write("\rElapsed time: %03d secondss %s" %(t, ""))
            sys.stdout.flush()
        sys.stdout.write("\rElapsed time: %03d seconds %s" %(t, "\n"))
        y = m*x + b
        # Store simulation
        self.outputs = {"x":x, "y":y}
        return
    
    def plot(self, filename="", display=False):
        """Conditionally imports the matplotlib library,
        and if possible, plots the experimental data 
        and the simulation data.
        
        :param filename: [description], defaults to ""
        :type filename: str, optional
        :param display: [description], defaults to False
        :type display: bool, optional
        """
        if self.configuration["matplotlib_version"]:
            from matplotlib import pyplot as plt    
        else:
            print("Cannot plot - matplotlib library not installed.")
            return
        # Create the figure
        my_fig = plt.figure(figsize=(16,8))
        has_content = False
        # Add the simulation, if possible
        if "x" in self.outputs and "y" in self.outputs:
            x = self.outputs["x"]
            y = self.outputs["y"]
            plt.plot(x, y, "-", label="sim")
            has_content=True
        # Add the (experimental) data, if possible
        if "x" in self.data and "y" in self.data:
            plt.plot(self.data["x"], self.data["y"], "o", label="data")
            has_content=True
        # Add the properties
        plt.xlabel("x here")
        plt.ylabel("y here")
        plt.legend()
        # Save figure, if filename provided
        if filename:
            my_fig.savefig(filename)
        # Show figure, if asked for
        if display:
            if has_content:
                plt.show()
            else:
                print("No content to plot.")
        plt.close()
        return

    def export_xlsx(self, filename):
        """
        XsX
        """
        # Create the file
        with open(filename, "w") as fh:
            fh.write("Este es un test\n")
            fh.write("TEST")
            print("Exported simulation as xlsx into file", filename)
        # Download the file
        
    def download(filename):
        """
        Utility to download file, using colab
        """
        if self.configuration["environment"]=="google_colab":
            from google.colab import files
            files.download(filename)
        return

        