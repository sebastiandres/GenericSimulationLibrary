# Generic Simulation Library

This is, unsurprinsingly, a Generic Simulation Library. 
It provides a framework to be extended for specific purposes.

A Framework to use Jupyter for SaaS (Simulation as a Service)

# Why (summary)
The main idea is to use jupyter notebook to provide a lightweight and for-dummies easy "Simulation as a Service". We propose a framework that provides simplicity: for the client to install and use, for the programmer to distribute and update, and for everyone to store and reproduce results. The framework can be personalized and extended for a particular simulation need.

# Longer Why (objective, outline, central thesis, key takeaways)
Why do we care so much? In 2008, we (a Biochemist and a Math-CS Engineer) started the development of numerical implementation of generic reaction diffusion equations of catalysts immobilized on small porous particles. Python was a great choice back then, as it provided a language that was simple and high level, but still fast enough. Nevertheless, the python installation, versioning and library updates were messy and required constant supervision and side by side work. We longed for a simpler method. Fast travel to 2020, where you can now run python code on your browser on a server. You can now really collaborate with anyone on the planet and make sure the simulation is being run exactly as supposed. We've been reflecting on the key elements that are required on a simulation framework that provides this kind of "SaaS behavior".
How could you make things as easy as possible for the other party while, as a developer, still been able to have full control on the code and guarantee the reproducibility of results?

The objective is to provide a working answer for the following constrains:
* Dealing with installation and versioning of python, jupyter and libraries.
* Simplifying the deployment and versioning of a specific piece of code (the custom simulation library).
* Exposing a simple interface to the final user to hied a (complex) numerical implementation.
* Allowing to store and share simulation results, so that they can be reproduced and analyzed.
* Allowing to use external computational resources, so that the simulation doesn't take a toll on your cheap notebook.

We think the former constraints can be solved with a code with the following characteristics:
* pip-installable library: this allows for a flexible approach. You can install nothing at all and run everything on google colab, or install it locally. But it's your call, and you are not forced to run everything on local (thanks free cloud providers!). This addresses for installation and versioning.  
* git-versioning and library versioning: smash those bugs and document the code increments. This addresses reproducibility and versioning. 
* simple interface: hide the complexity of the code with some OO to make it simple for the end user.
* simulation seed: the library should create a "simulation seed" that contains all the information (inputs, system and libraries configuration, options and outputs). This "simulation seed" can be stored and shared on itself, or together with a jupyter notebooks. This addresses the reproducibility.

Related articles:
* Code: the framework, a work in progress: https://github.com/sebastiandres/GenericSimulationLibrary
* Code: The old pypsdier library: https://bitbucket.org/sebastiandres/pypsdier/wiki/Home  and the new pypsdier library: https://github.com/sebastiandres/pypsdier 
* Code: The official pypi repo: https://pypi.org/project/Pypsdier/
* Article: Batch reactor performance for enzymatic synthesis of cephalexin: influence of catalyst enzyme loading and particle size, https://www.sciencedirect.com/science/article/pii/S0168165610005912?via%3Dihub
* Article: Effect of Internal Diffusional Restrictions on the Hydrolysis of Penicillin G: Reactor Performance and Specific Productivity of 6-APA with Immobilized Penicillin Acylase, https://link.springer.com/article/10.1007/s12010-011-9262-7
* Article: Analysis of the operational strategies for the enzymatic hydrolysis of food proteins in batch reactor, https://www.sciencedirect.com/science/article/abs/pii/S0260877415300303
* Post: Lorena Barba's group reproducibility syllabus: https://lorenabarba.com/blog/barbagroup-reproducibility-syllabus/

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
pip install git+https://github.com/sebastiandres/GenericSimulationLibrary.git
```

**Development Install**

Install it locally on your system with:
```
git clone https://github.com/sebastiandres/GenericSimulationLibrary.git
cd GenericSimulationLibrary
python setup.py install
```

**Install and uninstall**
Optionally, record the files installed, in case you want to remove them later:

```
python setup.py install --record installation_files.txt
```

Uninstall removing the files:

```
cat installation_files.txt | xargs sudo rm -rf
```
