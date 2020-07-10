# Generic Simulation Library

This is, unsurprinsingly, a Generic Simulation Library. 
It provides a framework to be extended for specific purposes.

# Test it

* In [colab](https://colab.research.google.com/drive/1mfSZQOhe7qq1C-YpfX5dDpSedXGVjz4e?usp=sharing)
* In [mybinder](https://mybinder.org/v2/gh/sebastiandres/GenericSimulationLibrary/master?filepath=GenericSimulationLibrary%2Ftest_notebook%2Ftest_mybinder.ipynb)

# Install it

*Easiest Install*
pip install git+https://github.com/jkbr/httpie.git


pip install --upgrade --force-reinstall pip==9.0.3

*Development Install*
python setup.py install --record installation_files.txt
#python setup.py install

Uninstall
cat installation_files.txt | xargs sudo rm -rf

# Where has been used?

See [pypsdier](https://github.com/sebastiandres/pypsdier) library for an example of a real numerical implementation using this framework.