Examples
=============

Example in Google colab
************************

In `Google Colab <https://colab.research.google.com/drive/1mfSZQOhe7qq1C-YpfX5dDpSedXGVjz4e?usp=sharing>`_. 
Requires a google account (but it's worth it :).

Example in mybinder
*********************

In `MyBinder <https://mybinder.org/v2/gh/sebastiandres/GenericSimulationLibrary/master?filepath=GenericSimulationLibrary%2Ftest_notebook%2Ftest_mybinder.ipynb>`_.
Does not requires any acount, but does not stores result.

Code example
*********************
To run it, you need to install the library. 

To run and save a simulation:

.. code-block:: python

    from GenericSimulationLibrary import SimulationInterface
    # Defines the inputs for the simulation and output file
    inputs = {
            "x_min":0, 
            "x_max":10, 
            "N_points":30,
            "m":1.5,
            "b":1,
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
    SI.save(filename="test_1.sim")  # Save the simulation
    
To load a simulation and plot the results:

.. code-block:: python

    from GenericSimulationLibrary import SimulationInterface
    SI = SimulationInterface()      # Create a new simulation object
    SI.load(filename="test_1.sim")  # Add the inputs and data
    SI.status()                     # Print the status of simulation
    SI.plot()                       # Plot the results 
    SI.export_xlsx("test_1.xlsx")   # Export the results as a xlsx

As you can see, all you need is to define the inputs and plot options, and run the simulation. 
Libraries and outputs are silently handled. 
Saving, plotting or exporting the results is trivially easy for the user.
