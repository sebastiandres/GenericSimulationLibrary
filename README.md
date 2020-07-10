# Generic Simulation Library

This is, unsurprinsingly, a Generic Simulation Library. 
It provides a framework to be extended for specific purposes.

# Test it

* In [colab](https://colab.research.google.com/drive/1mfSZQOhe7qq1C-YpfX5dDpSedXGVjz4e?usp=sharing)
* In [mybinder](https://mybinder.org/v2/gh/sebastiandres/GenericSimulationLibrary/master?filepath=GenericSimulationLibrary%2Ftest_notebook%2Ftest_mybinder.ipynb)

# Where has been used?

See [pypsdier](https://github.com/sebastiandres/pypsdier) library for an example of a real numerical implementation using this framework.

# How to use it
You need to define the inputs and data, and run the simulation. Libraries and outputs are silently handled.
An minimal example:

```
from GenericSimulationLibrary import SimulationInterface
# Defines the inputs for the simulation and output file
inputs = {
         "x_min":0, 
         "x_max":10, 
         "N_points":30,
         "m":1.5,
         "b":1,
         "filename":"test_1.sim"
        }
# Defines the experimental data (to be plotted)
data = {
         "x":[0,1,2,3], 
         "y":[0,1,2,3], 
         "plot_options":None
       }
# Now use the library
SI = SimulationInterface()      # Create a new simulation object
SI.new(inputs, data)            # Add the inputs and data
SI.status()                     # Print the status of simulation
SI.simulate()                   # Do the simulation
SI.plot()                       # Plot the results 
SI.export_xlsx("test_3.xlsx")   # Export the results as a xlsx
SI.save()                       # Save the simulation
``` 

# Install it

**Easiest Install**

```
pip install git+https://github.com/jkbr/httpie.git
```

pip install --upgrade --force-reinstall pip==9.0.3

**Development Install**

Install it on your system with:
```
#python setup.py install
```

Optionally, record the files installed, in case you want to remove it later.
```
python setup.py install --record installation_files.txt
```

**Uninstall**

cat installation_files.txt | xargs sudo rm -rf

