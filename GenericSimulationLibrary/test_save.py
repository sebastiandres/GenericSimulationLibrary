from SimulationInterface import SimulationInterface
parameters = {
                "x_min":0, 
                "x_max":10, 
                "x_Npoints":30,
                "m":1.5,
                "b":1,
             }
data = {
        "x":[0,1,2,3], 
        "y":[0,1,2,3], 
        "plot_options":None
        }

JSE = SimulationInterface()
JSE.status()
JSE.new(parameters, data)
JSE.simulate()
JSE.save()