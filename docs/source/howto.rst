How to use it
==============

You should start by cloning the repo: `<https://github.com/sebastiandres/GenericSimulationLibrary>`_.

.. code-block:: bash

    git clone https://github.com/sebastiandres/GenericSimulationLibrary.git

Distribution
****************

After cloning the deparment, dont forget to version control. It's not optional. 
This is needed for versioning and also for the documentation.

Add it to github, bitbucket or other repository.

Upload it to pypi.

Personalization
****************

Start by replacing **GenericSimulationLibrary** by your library name.

Replace **SimulationInterface** with other name if you like.

Simulation code
*****************

Edit the file `GenericSimulationLibrary/src/simulation_interface.py`.

Add other files to `GenericSimulationLibrary/src/` if you need and 
don't forget to edit `__init__.py` if needed.

Documentation
***************

The documentation is stored at `GenericSimulationLibrary/docs/source/` in all the rst files.
You should personalize all those files.

To rebuilt the documentation, at the path `GenericSimulationLibrary/docs/` execute:

.. code-block:: bash

    make clean
    make htmls

Go to the site read-the-docs and import your library documentation to make it public.